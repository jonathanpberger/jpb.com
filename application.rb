# encoding: utf-8

require 'rubygems'
require 'haml'
require 'sinatra/base'

class Application < Sinatra::Base
  configure do
    enable :static

    set :views,  File.join(File.dirname(__FILE__), 'views')
    set :public, File.join(File.dirname(__FILE__), 'public')
  end

  helpers do
    # ...
  end

  not_found do
    haml 'Not found'
  end

  error do
    haml "Error (#{request.env['sinatra.error']})"
  end

  get '/' do
    haml :index
  end

  get '/bio' do
    haml :bio
  end

  get '/talks' do
    haml :talks
  end

  get '/blog' do
    redirect "http://jonathanpberger.wordpress.com"
  end

  ["/cv", "/resume", "/resume.pdf"].each do |path|
    get path do
      redirect "http://jonathanpberger.com/cv.pdf"
    end
  end

  get '/code_management' do
    haml :code_management
  end

  get '/code_as_lit' do
    haml :code_as_lit
  end
end

