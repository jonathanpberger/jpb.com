# JPB.com Jekyll Migration

## Goals
- Convert Rack app to Jekyll for GitHub Pages deployment
- Preserve HAML usage
- Keep existing Markdown content
- Maintain current styling
- Keep current routing/URLs working

## Technical Requirements
- Use Jekyll with HAML plugin
- Preserve all current routes from application.rb
- Maintain redirects (blog, calendar, etc)
- Ruby version selection criteria:
  - Check EOL dates when selecting versions
  - Prefer versions with longer support windows
  - Balance stability with maintenance lifecycle
  - Consider GitHub Pages compatibility
  - Jekyll is a static site generator, doesn't need cutting-edge features
  - Use single source of truth for version management (DRY)
  - Must be compatible with GitHub Pages deployment

## Migration Steps
1. Set up Jekyll structure
2. Convert views to Jekyll layout/includes
3. Move static assets
4. Configure GitHub Pages
5. Test all routes and redirects

## Notes
- Uses Sinatra for routing
- Has PDF redirects for CV/resume
- Required redirects from Rack app:

## Jekyll Directory Structure
- Content pages go in _pages directory
  - About, events, talks, and other content pages
  - Each page needs front matter with layout specified
  - Convert HAML files to HTML when moving to _pages
  - Use .html extension for all pages
  - Add permalink in front matter to maintain URLs
  - Must include _pages directory in config.yml includes list
  - Example front matter:
    ```yaml
    ---
    layout: default
    title: Page Title
    permalink: /url-path/
    ---
    ```
  - Pages won't be served without both:
    1. Correct permalink in front matter
    2. Directory listed in config.yml includes
- Posts go in _posts directory (dated blog posts)
- Layouts go in _layouts directory
- Include snippets go in _includes directory
- Assets (CSS, JS, images) go in assets directory
  - Preferred over keeping in root or public_folder
- Data files go in _data directory
- Collections configured in _config.yml
  - Custom content types beyond posts/pages
  - Each collection gets its own directory (e.g., _talks)

  - /blog -> jonathanpberger.wordpress.com
  - /cv, /resume, /resume.pdf -> /cv.pdf  
  - /cal, /calendar, /calendly -> calendly.com/jonathanpberger
- Jekyll redirect implementation:
  - Use jekyll-redirect-from plugin
  - Add redirect_from front matter to target pages
  - For external redirects, create HTML files with meta refresh
- Jekyll asset handling differs from Rack:
  - Assets must be in root public folder or _site directory
  - CSS/JS paths should be relative to site root
  - Asset pipeline differs from Rack's static file serving
  - Font files must be in /fonts directory at root level
  - Image paths need /images prefix from root
  - All asset paths should start with forward slash
  - Public folder contents should be copied to root for proper serving
  - Links to internal pages need forward slash prefix (e.g., /events not events)
## Template Setup
- Use plain HTML templates instead of HAML
- HAML processing was attempted but abandoned due to persistent issues
- Layout files:
  - Must be in _layouts directory
  - Use .html extension
  - Content inserted via {{ content }} Liquid tag
- Regular pages:
  - Need layout: default in front matter
  - Use .html extension or .md for Markdown
- HAML files require proper front matter to be processed:
  - Even empty front matter (just `---`) is required
  - Layout files must specify layout: null
  - Regular pages should specify layout: default
- Jekyll's asset handling:
  - CSS/JS/image paths must be relative to site root
  - Use absolute paths starting with forward slash
  - Example: /css/style.css not css/style.css

## Troubleshooting
- If HAML isn't rendering:
  - Check file extensions (.html.haml not just .haml)
  - Verify front matter exists and is properly formatted
  - Ensure layout files have layout: null
  - Check Jekyll plugin configuration in _config.yml
  - Variables like page and site need special handling in HAML templates
