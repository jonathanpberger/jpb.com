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
    sh "bundle exec jekyll build"
    sh "git push origin HEAD:gh-pages"
  when "prod"
    sh "bundle exec jekyll build"
    sh "git push origin HEAD:production"
  else
    puts "Invalid environment. Use 'staging' or 'prod'"
  end
end

task :default => [:serve]
