# WordPress to Jekyll Migration Guide

This guide will help you migrate your WordPress blog posts to this Jekyll site.

## Step 1: Export from WordPress

1. Log in to your WordPress.com dashboard
2. Go to **Tools** → **Export**
3. Select **All content** and click **Download Export File**
4. Save the XML file (usually named something like `jonathanpberger.wordpress.2024-11-14.xml`)

## Step 2: Place the Export File

Save the WordPress XML export file to this repository directory:
```bash
/home/user/jpb.com/wordpress-export.xml
```

(You can name it whatever you want, we just need it in this directory)

## Step 3: Run the Migration Script

```bash
python3 wordpress_to_jekyll.py wordpress-export.xml
```

This will:
- Parse all published posts from the WordPress export
- Convert HTML content to Markdown
- Create properly formatted Jekyll posts in the `_posts/` directory
- Set up redirects from old WordPress URLs
- Preserve categories, tags, and metadata

## Step 4: Review the Generated Posts

Check the `_posts/` directory for your migrated posts. Each will be named:
```
YYYY-MM-DD-post-title-slug.md
```

Review a few posts to make sure the conversion worked correctly.

## Step 5: Handle Images and Media

The script converts post content but doesn't download images. You'll need to:

1. Check posts for images that reference WordPress URLs
2. Download those images
3. Save them to `/assets/images/blog/`
4. Update the image paths in the posts

Or, you can leave the images on WordPress.com (they'll still work via hotlinking).

## Step 6: Test Locally

Build and serve the site locally to test:

```bash
bundle exec jekyll serve
```

Then visit http://localhost:4000/blog/ to see your posts.

## Step 7: Deploy

Once everything looks good, commit and push:

```bash
git add _posts/ _config.yml _layouts/post.html _pages/blog.html assets/css/style.css
git commit -m "Migrate blog from WordPress to Jekyll"
git push
```

## What Was Set Up

The migration has already configured:

- **Blog structure**: Created `_posts/` directory for posts
- **Post layout**: Created `_layouts/post.html` for individual post pages
- **Blog index**: Updated `_pages/blog.html` to list all posts
- **Styling**: Added blog-specific CSS matching your site's aesthetic
- **Config**: Updated `_config.yml` with blog settings and permalink structure
- **Plugins**: Added jekyll-feed for RSS and jekyll-seo-tag for SEO

## URL Structure

Posts will be available at URLs like:
```
/blog/2016/09/23/building-with-atoms-building-with-bits/
```

The old WordPress URLs will redirect to the new ones using the `redirect_from` plugin.

## Troubleshooting

**Posts not showing up?**
- Make sure the file is in `_posts/` and named `YYYY-MM-DD-title.md`
- Check that the front matter has `layout: post`
- Try rebuilding: `bundle exec jekyll clean && bundle exec jekyll serve`

**Formatting issues?**
- The HTML-to-Markdown conversion is basic
- You may need to manually fix complex formatting
- Check code blocks, lists, and embedded content

**Images not loading?**
- Either download them to `/assets/images/blog/`
- Or leave them on WordPress.com (they should still work)

## Need Help?

If you run into issues, check:
- Jekyll docs: https://jekyllrb.com/docs/posts/
- The generated post files in `_posts/` for examples
