require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
  options = {
    :assume_extension => true,
    :allow_hash_href => true,
    :check_favicon => true,
    :check_html => true,
    :check_img_http => true,
    :check_opengraph => true,
    :disable_external => true, # Disable external checks for faster testing
    :enforce_https => true,
    :only_4xx => true,
    :file_ignore => [
      %r{_site/public_folder/.*}  # Ignore all files in _site/public_folder for now
    ]
  }
  HTMLProofer.check_directory("./_site", options).run
end


task :visit do
  sh "open https://jonathanpberger.github.io/jpb.com"
end

# Serve tasks
task :s => :serve
# Serve tasks
task :s => :serve
task :serve do
  sh "pkill -f jekyll || true"  # Kill existing jekyll processes, don't error if none
  sh "bundle exec jekyll serve"
end

# Deploy tasks
task :deploy, [:env] do |t, args|
  env = args[:env] || "staging"
  case env
  when "staging"
    # GitHub Pages always uses JEKYLL_ENV=production
    sh "JEKYLL_ENV=production bundle exec jekyll build"
    sh "git push origin HEAD:gh-pages"
    sh "open https://github.com/jonathanpberger/jpb.com/actions/"
  when "prod"
    # GitHub Pages always uses JEKYLL_ENV=production
    sh "JEKYLL_ENV=production bundle exec jekyll build"
    sh "git push origin HEAD:gh-pages"
    sh "open https://github.com/jonathanpberger/jpb.com/actions/"
  else
    puts "Invalid environment. Use 'staging' or 'prod'"
  end
end

task :default => [:serve]
