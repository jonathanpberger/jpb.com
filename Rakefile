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

task :serve do
  sh "bundle exec jekyll serve"
end

task :default => [:serve]
