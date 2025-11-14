#!/usr/bin/env python3
"""
WordPress to Jekyll Migration Script
Converts a WordPress XML export to Jekyll markdown posts
"""

import xml.etree.ElementTree as ET
import re
import os
from datetime import datetime
from html import unescape
import sys

def slugify(text):
    """Convert text to a URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def html_to_markdown(html_content):
    """Basic HTML to Markdown conversion"""
    if not html_content:
        return ""

    # Unescape HTML entities
    content = unescape(html_content)

    # Convert common HTML tags to Markdown
    # Headers
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', content, flags=re.DOTALL)

    # Bold and italic
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)

    # Links
    content = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)

    # Code blocks
    content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', content, flags=re.DOTALL)
    content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.DOTALL)

    # Lists
    content = re.sub(r'<ul[^>]*>', '', content)
    content = re.sub(r'</ul>', '\n', content)
    content = re.sub(r'<ol[^>]*>', '', content)
    content = re.sub(r'</ol>', '\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)

    # Paragraphs
    content = re.sub(r'<p[^>]*>', '\n', content)
    content = re.sub(r'</p>', '\n', content)

    # Line breaks
    content = re.sub(r'<br\s*/?>', '\n', content)

    # Blockquotes
    content = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'> \1', content, flags=re.DOTALL)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Clean up excessive whitespace
    content = re.sub(r'\n\n\n+', '\n\n', content)
    content = content.strip()

    return content

def parse_wordpress_export(xml_file):
    """Parse WordPress XML export and extract posts"""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # WordPress uses namespaces
    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'wp': 'http://wordpress.org/export/1.2/',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }

    posts = []

    for item in root.findall('.//item'):
        post_type = item.find('wp:post_type', namespaces)
        post_status = item.find('wp:status', namespaces)

        # Only process published posts (not pages, drafts, etc.)
        if post_type is not None and post_type.text == 'post' and \
           post_status is not None and post_status.text == 'publish':

            title = item.find('title').text or 'Untitled'
            link = item.find('link').text or ''
            pub_date = item.find('pubDate').text
            creator = item.find('dc:creator', namespaces)
            content_encoded = item.find('content:encoded', namespaces)

            # Parse date
            date_obj = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %z')

            # Get categories and tags
            categories = []
            tags = []
            for category in item.findall('category'):
                domain = category.get('domain')
                if domain == 'category':
                    categories.append(category.text)
                elif domain == 'post_tag':
                    tags.append(category.text)

            # Get post slug from WordPress or create from title
            post_name = item.find('wp:post_name', namespaces)
            slug = post_name.text if post_name is not None and post_name.text else slugify(title)

            # Convert content to markdown
            content_html = content_encoded.text if content_encoded is not None else ''
            content_md = html_to_markdown(content_html)

            posts.append({
                'title': title,
                'date': date_obj,
                'slug': slug,
                'author': creator.text if creator is not None else 'Jonathan Berger',
                'categories': categories,
                'tags': tags,
                'content': content_md,
                'original_url': link
            })

    return posts

def create_jekyll_post(post, posts_dir='_posts'):
    """Create a Jekyll markdown post file"""
    os.makedirs(posts_dir, exist_ok=True)

    # Create filename: YYYY-MM-DD-slug.md
    date_str = post['date'].strftime('%Y-%m-%d')
    filename = f"{date_str}-{post['slug']}.md"
    filepath = os.path.join(posts_dir, filename)

    # Create front matter
    front_matter = ['---']
    front_matter.append(f"layout: post")
    front_matter.append(f"title: \"{post['title']}\"")
    front_matter.append(f"date: {post['date'].strftime('%Y-%m-%d %H:%M:%S %z')}")

    if post['author']:
        front_matter.append(f"author: \"{post['author']}\"")

    if post['categories']:
        front_matter.append(f"categories: [{', '.join(post['categories'])}]")

    if post['tags']:
        tags_str = ', '.join([f'"{tag}"' for tag in post['tags']])
        front_matter.append(f"tags: [{tags_str}]")

    # Add redirect from old WordPress URL if available
    if post['original_url']:
        # Extract path from WordPress URL
        wordpress_path = post['original_url'].replace('https://jonathanpberger.wordpress.com', '')
        if wordpress_path and wordpress_path != '/':
            front_matter.append(f"redirect_from:")
            front_matter.append(f"  - {wordpress_path}")

    front_matter.append('---')
    front_matter.append('')

    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(front_matter))
        f.write(post['content'])

    print(f"Created: {filename}")
    return filepath

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 wordpress_to_jekyll.py <wordpress-export.xml>")
        sys.exit(1)

    xml_file = sys.argv[1]

    if not os.path.exists(xml_file):
        print(f"Error: File '{xml_file}' not found")
        sys.exit(1)

    print(f"Parsing WordPress export: {xml_file}")
    posts = parse_wordpress_export(xml_file)

    print(f"\nFound {len(posts)} published posts")
    print("\nCreating Jekyll posts...")

    for post in posts:
        create_jekyll_post(post)

    print(f"\n✓ Migration complete! Created {len(posts)} posts in _posts/")
    print("\nNext steps:")
    print("1. Review the generated posts in _posts/")
    print("2. Check for any formatting issues")
    print("3. Download and organize any images/media")
    print("4. Test locally with: bundle exec jekyll serve")

if __name__ == '__main__':
    main()
