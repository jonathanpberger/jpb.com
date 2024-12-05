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
      %r{public_folder/.*}  # Ignore legacy content
    ]
  }
  HTMLProofer.check_directory("./_site", options).run
end

task :test_source do
  options = {
    :assume_extension => true,
    :allow_hash_href => true,
    :check_favicon => true,
    :check_html => true,
    :check_img_http => true,
    :check_opengraph => true,
    :disable_external => true,
    :enforce_https => true,
    :only_4xx => true,
    :file_ignore => [
      %r{public_folder/.*}  # Ignore legacy content
    ],
    :directory_index_file => true  # Use directory index files
  }
  Dir.glob(['**/*.html', '**/*.md']) do |file|
    next if file.start_with?('_site/')
    HTMLProofer.check_file(file, options).run
  end
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
  Rake::Task["update_git_sha"].execute
  sh "JEKYLL_ENV=development bundle exec jekyll clean && JEKYLL_ENV=development bundle exec jekyll serve --baseurl=''"
end

# Deploy tasks
# Update GIT_SHA before building
task :update_git_sha do
  sha = `git rev-parse HEAD`.strip
  File.write('_includes/GIT_SHA', sha)
end

task :deploy, [:env] do |t, args|
  env = args[:env] || "staging"
  case env
  when "staging"
    # GitHub Pages always uses JEKYLL_ENV=production
    Rake::Task["update_git_sha"].execute
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
