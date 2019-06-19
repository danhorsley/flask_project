"""SQLAlchemy models for twitoff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
  """Twitter users that we pull and analyse tweets for"""
  id = DB.Column(DB.Integer, primary_key=True)
  name = DB.Column(DB.String(15), nullable = False)
  
  def __repr__(self):
    return '<User {}.'.format(self.name)
  
class Tweet(DB.Model):
  """Tweets"""
  id = DB.Column(DB.Integer, primary_key=True)
  text = DB.Column(DB.Unicode(280))
  
   def __repr__(self):
    return '<Tweet {}.'.format(self.text)
  
  

  
