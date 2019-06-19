"""main application and routing logic for twitoff"""
from flask import flask

def create_app():
  """Create and configure instance of the Flask application"""
    @app.route('/')
    def root():
      return 'Welcome to TwitOff!!'
    
  return app
