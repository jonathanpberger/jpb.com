require "jekyll-import"
require "fileutils"
require "yaml"

def rewrite_image_paths(content)
  # Replace WordPress media URLs with local Jekyll paths
  content.gsub(
    /https?:\/\/jonathanpberger\.wordpress\.com\/wp-content\/uploads/,
    '/assets/media_export/wp-content/uploads'
  )
end

BACKUP_DIR = "jonathanpbergercomblog.wordpress.2025-02-07.000"
SOURCE_XML = File.join(BACKUP_DIR, "wordpress.xml")
TARGET_XML = "wordpress.xml"
POSTS_DIR = File.expand_path("../../_posts", __FILE__)

# Configure import options
options = {
  "dbname"   => nil,
  "socket"   => nil,
  "user"     => nil,
  "password" => nil,
  "host"     => nil,
  "prefix"   => nil,
  "clean_entities" => true,
  "comments"      => true,
  "categories"    => true,
  "tags"          => true,
  "extension"     => "md",
  "status"        => ["publish"],
  "import_type"   => "xml",
  "file"          => TARGET_XML
}

begin
  puts "//////////// Starting WordPress import..."
  puts "Copying #{SOURCE_XML} to #{TARGET_XML}"
  
  raise "Source XML file not found!" unless File.exist?(SOURCE_XML)
  FileUtils.cp(SOURCE_XML, TARGET_XML)
  
  # Create _posts directory if it doesn't exist
  FileUtils.mkdir_p(POSTS_DIR)
  
  JekyllImport::Importers::WordpressDotCom.run(options)
  
  # Move posts from scripts/_posts to root _posts
  Dir.glob("_posts/*.{html,md}") do |post|
    filename = File.basename(post)
    target = File.join(POSTS_DIR, filename)
    puts "Moving #{post} to #{target}..."
    
    content = File.read(post)
    content = rewrite_image_paths(content)
    File.write(target, content)
    File.delete(post)
  end
  
  puts "//////////// Import completed successfully!"
rescue => e
  puts "Error during import: #{e.message}"
  puts e.backtrace
ensure
  # Clean up temporary files
  File.delete(TARGET_XML) if File.exist?(TARGET_XML)
  FileUtils.rm_rf("_posts") if Dir.exist?("_posts")
end