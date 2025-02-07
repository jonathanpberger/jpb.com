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
  "file"          => "jonathanpbergercomblog.wordpress.2025-02-07.000.xml"  # Updated to use local path
}

begin
  puts "//////////// Starting WordPress import..."
  JekyllImport::Importers::WordpressDotCom.run(options)
  
  # Post-process the imported files to fix image paths
  Dir.glob("../_posts/*.md") do |post|
    puts "Processing #{post}..."
    content = File.read(post)
    File.write(post, rewrite_image_paths(content))
  end
  
  puts "//////////// Import completed successfully!"
rescue => e
  puts "Error during import: #{e.message}"
  puts e.backtrace
end