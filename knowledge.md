# JPB.com Jekyll Migration

## Goals
- Convert Rack app to Jekyll for GitHub Pages deployment
- Preserve HAML usage
- Keep existing Markdown content
  - Production: jonathanpberger.com (future)
  - Use Jekyll environments to manage different configurations:
    - Development: JEKYLL_ENV=development (local)
    - Staging: JEKYLL_ENV=staging (github.io)
    - Production: JEKYLL_ENV=production (custom domain)
  - Configure baseurl and other environment-specific settings in _config/{env}.yml
  - Never manually edit baseurl in _config.yml
  - Run locally with: JEKYLL_ENV=development bundle exec jekyll serve
  - Deploy to staging with: JEKYLL_ENV=staging bundle exec jekyll build
- Maintain current styling
- Keep current routing/URLs working

## Technical Requirements
- Avoid non-standard Jekyll plugins that aren't supported by GitHub Pages
- Preserve all current routes from application.rb
- Maintain redirects (blog, calendar, etc)
- Deployment environments:
  - Staging: jonathanpberger.github.io/jpb.com
  - Keep baseurl configured for staging
  - Asset paths must work in both environments
- Deployment strategy:
    - Staging: GitHub Pages always uses `JEKYLL_ENV=production`
    - Production: `JEKYLL_ENV=production bundle exec jekyll build`
  - Configuration in _config.yml uses environment-specific settings
  - GitHub Pages specific requirements:
    - Always runs in production environment (JEKYLL_ENV=production)
    - Cannot override JEKYLL_ENV via config
    - Must explicitly set JEKYLL_ENV in deployment scripts if different environment is needed
  - Use Jekyll environments to manage different configurations:
    - Development (default): `JEKYLL_ENV=development bundle exec jekyll serve`
    - Always runs in production environment (JEKYLL_ENV=production)
    - Cannot override JEKYLL_ENV on GitHub Pages
    - Our "staging" deployment still uses production environment
    - Configure environment-specific settings in _config.yml under environment names
    - Access settings with site[jekyll.environment].baseurl syntax
    - All asset paths must include baseurl for project pages
  - Use Rake tasks for consistent workflow:
    - `rake serve` or `rake s`: Run local development server
    - `rake deploy`: Deploy to staging (GitHub Pages)
    - `rake deploy prod`: Deploy to production (future)
  - All commands should use appropriate Jekyll environment
  - Never use raw Jekyll commands directly
  - Always use rake tasks for:
    - Local development
    - Building
    - Deployment
    - Testing
  - This ensures consistent behavior and proper environment setup
  - All URLs should use HTTPS where possible
  - No need to modify _config.yml between environments
  - Asset paths automatically adjust based on environment
  - Important: Jekyll's exclude in _config.yml only affects build process
    - Git operations (like submodules) are not affected by Jekyll excludes
    - Must handle Git cleanup separately from Jekyll configuration
    - When removing legacy content:
      - Jekyll exclude prevents files from being built/copied to _site
      - Git still tracks excluded files until explicitly untracked
      - Handle submodules separately from regular files
      - Prefer cleaning Git references over deleting content
- GitHub Pages compatibility requirements:
  - Two deployment options:
    1. Default GitHub Pages build:
      - Must use github-pages gem
      - Restricted to specific gem versions
      - Limited to whitelisted plugins only
      - Cannot override environment settings
    2. GitHub Actions build (preferred):
      - Full control over dependencies
      - Can use any Jekyll version
      - Supports all plugins
      - Still runs in production environment
  - Use only GitHub-supported plugins if using default build
  - Avoid custom plugins like jekyll-haml unless using Actions
  - Test builds locally with same environment as GitHub Pages
  - Asset paths must include baseurl when site is not at root
  - Configure baseurl in _config.yml for project pages
  - Test asset paths with both local Jekyll serve and GitHub Pages URL
  - Use relative paths (./assets/*) instead of absolute paths (/assets/*) for GitHub Pages project sites
  - Relative paths work better than absolute paths with repository prefixes
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

## Environment Configuration
- Keep baseurl configuration DRY:
  - Set baseurl in _config.yml for GitHub Pages compatibility
  - Override with --baseurl flag for local development
  - Use {{ site.baseurl }} consistently in templates
  - Avoid environment-specific baseurl settings
  - Debug with /info page to verify correct values

## Ruby/Rake Setup
- Required gems for development:
  - `rake` for task running
  - `jekyll` for site generation
  - `github-pages` for GitHub Pages compatibility
  - `webrick` for Ruby 3+ compatibility
- Common issues:
  - GitHub Pages always uses JEKYLL_ENV=production
  - Local development should use JEKYLL_ENV=development
  - Must override baseurl with --baseurl='' for local development
  - Kill existing Jekyll processes before serving: `pkill -f jekyll`
- Default baseurl/url provide fallback values
- Environment settings override defaults when JEKYLL_ENV is set
- Use debug page (/info) to verify environment configuration
- DRY Principles:
  - Avoid scattering `site[jekyll.environment]` throughout templates
  - Prefer centralizing environment-specific logic in layouts or includes
  - Consider creating custom Jekyll plugins or Liquid includes for environment handling
- DRY Principles:
  - Avoid scattering `site[jekyll.environment]` throughout templates
  - Prefer centralizing environment-specific logic in layouts or includes
  - Consider creating custom Jekyll plugins or Liquid includes for environment handling
  - Never maintain environment-specific paths (like baseurl) in individual templates
  - Always handle environment configuration at config level
  - Use Jekyll filters or includes if path manipulation is needed
- Common environment issues:
  - Incorrect JEKYLL_ENV setting
  - Missing environment-specific config
  - Default values overriding environment settings
- Three environments supported:
  - Development: Local development (JEKYLL_ENV=development)
  - Staging: GitHub Pages testing (JEKYLL_ENV=staging)
  - Production: Live site (JEKYLL_ENV=production)
- Environment-specific settings configured in _config.yml:
  ```yaml
  development:
    baseurl: ""
    url: "https://localhost:4000"
  staging:
    baseurl: "/jpb.com"  # for GitHub Pages project site
    url: "https://jonathanpberger.github.io"
# Custom Domain Setup
When moving from GitHub Pages (jonathanpberger.github.io/jpb.com) to custom domain (jonathanpberger.com):

1. Update _config.yml production settings:
```yml
production:
  baseurl: ""  # Must be empty string for custom domain
  url: "https://jonathanpberger.com"
```

Important: When moving to custom domain:
- Clear baseurl in production config (empty string, not "/")
- Update all asset paths to use site.baseurl
- Test both with and without trailing slashes
- Common issues:
  - CSS not loading: check site.baseurl in asset paths
  - 404s: verify baseurl is truly empty in production
  - Mixed content: ensure all URLs use https://

2. Configure GitHub Pages:
   - Go to repo Settings > Pages
   - Under "Custom domain" enter: jonathanpberger.com
   - Enable "Enforce HTTPS"
   - Wait for SSL certificate (may take up to 24 hours)

3. Configure GoDaddy DNS:
   - Add CNAME record:
     - Host: @ or www
     - Points to: jonathanpberger.github.io
   - Add A records for GitHub Pages IPs:
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
   - TTL: 600 seconds or lowest available
   - DNS propagation may take 24-48 hours

4. Verify Setup:
   - Check DNS propagation: https://www.whatsmydns.net
   - Verify HTTPS certificate active
   - Test both www and apex domain

production:
  baseurl: ""
  url: "https://jonathanpberger.com"
  ```
- Access via: `{{ site[jekyll.environment].baseurl }}`
- Debug environment issues:
  - Check JEKYLL_ENV is set correctly
  - Verify all asset/link paths use site[jekyll.environment].baseurl
  - Create debug page to show Jekyll variables if needed
- Common places to check:
  - Image src attributes
  - Asset paths (CSS, JS)
  - Internal links
  - Redirects
  - PDF/document links

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
  - Jekyll convention is to use /assets directory at project root
  - Subdirectories like /assets/images, /assets/css, /assets/js, /assets/fonts
  - Do not use /public_folder (Rack convention) or root-level asset directories
  - All asset paths in HTML/CSS should be absolute from site root (e.g., /assets/images/photo.jpg)
  - Important: Jekyll's exclude in _config.yml only affects build process
    - Git operations (like submodules) are not affected by Jekyll excludes
    - Must handle Git cleanup separately from Jekyll configuration
    - When removing legacy content:
      - Jekyll exclude prevents files from being built/copied to _site
      - Git still tracks excluded files until explicitly untracked
      - Handle submodules separately from regular files
      - Prefer cleaning Git references over deleting content
  - Migration from Rack:
    - Move /css -> /assets/css
    - Move /images -> /assets/images 
    - Move /js -> /assets/js
    - Move /fonts -> /assets/fonts
    - Update all @font-face src paths in CSS to use /assets/fonts/
    - Update all asset references to use /assets prefix
    - Remove /public_folder after migration complete
- Data files go in _data directory
- Collections configured in _config.yml
  - Custom content types beyond posts/pages
  - Each collection gets its own directory (e.g., _talks)

  - /blog -> jonathanpberger.wordpress.com
  - /cv, /resume, /resume.pdf -> /cv.pdf  
  - /cal, /calendar, /calendly -> calendly.com/jonathanpberger  - Jekyll redirect implementation:
    - Use jekyll-redirect-from plugin
    - Add redirect_from front matter to target pages
    - For external redirects, create HTML files with meta refresh
    - Required redirects from Rack app must be preserved:
      - /cv -> /cv.pdf (internal file redirect)
      - /resume -> /cv.pdf
      - /resume.pdf -> /cv.pdf
      - /blog -> jonathanpberger.wordpress.com (external redirect)
      - /cal, /calendar, /calendly -> calendly.com/jonathanpberger
    - Implementation patterns:
      - For internal file redirects: Use redirect_to in _config.yml
      - For external redirects: Use redirect_from plugin or meta refresh
  - Required redirects from Rack app must be preserved:
    - /cv -> /cv.pdf (internal file redirect)
    - /resume -> /cv.pdf
    - /resume.pdf -> /cv.pdf
    - /blog -> jonathanpberger.wordpress.com (external redirect)
    - /cal, /calendar, /calendly -> calendly.com/jonathanpberger
  - Implementation patterns:
    - For internal file redirects: Use redirect_to in _config.yml
    - For external redirects: Use redirect_from plugin or meta refresh
- Jekyll asset handling differs from Rack:
  - Assets must be in root public folder or _site directory
  - CSS/JS paths should be relative to site root
  - Asset pipeline differs from Rack's static file serving
  - Font files must be in /fonts directory at root level
  - Image paths need /images prefix from root
  - All asset paths should start with forward slash
  - Public folder contents should be copied to root for proper serving
  - Links to internal pages need forward slash prefix (e.g., /events not events)
  - All asset and internal link paths must use site.baseurl prefix for proper staging/production support
  - Common paths to check:
    - Image src attributes
    - CSS/JS file includes
    - Internal page links
    - Font file paths
    - PDF and document links
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

## Testing Strategy
- Use html-proofer for automated testing
- Display git SHA on info page for deployment verification
  - SHA must be updated automatically in all environments (dev, staging, prod)
  - Use Rake task :update_git_sha before all builds
  - Critical for verifying correct deployment version
- Legacy presentation decks in public_folder should be excluded from tests
- Focus testing on main site content:
  - Navigation and internal links
  - Core pages (_pages directory)
  - Layout templates
  - Asset references
- External link checking can be disabled during development with `:disable_external => true`
- Testing considerations during migration:
  - Separate concerns between main site and legacy content
  - Legacy presentation decks may have outdated HTML patterns
  - Use file_ignore patterns to exclude legacy content: `%r{_site/public_folder/.*}`
  - Image tests check both existence and accessibility (alt text)
  - All external links should use HTTPS where possible
```
