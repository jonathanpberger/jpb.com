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
- Jekyll asset handling differs from Rack:
  - Assets must be in root public folder or _site directory
  - CSS/JS paths should be relative to site root
  - Asset pipeline differs from Rack's static file serving
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
