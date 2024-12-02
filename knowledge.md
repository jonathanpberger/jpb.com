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

## Routing & Redirects
- Prefer configuration-based routing over Jekyll's redirect-from gem
- Never use HTML stub files for redirects
- Use _config.yml permalinks and redirect_to for all routing
- Do not use Jekyll's frontmatter-based redirects
- CV and similar document routes should point directly to files via config
- External redirects (blog, calendar) need custom handling
