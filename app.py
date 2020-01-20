from flask import Flask, request, jsonfify
from flask_sqlalchemy import flask_sqlalchemy
from flask_cors import CORS
from flask_heroku import Heroku
import os

app = Flask(__name__)
heroku = Heroku(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

CORS(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Meme(db.Model):
  __tablename__ = "memes"
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(50))
  image = db.Column(db.String(500))
  favorite = db.Column(db.Boolean)

  def __init__(self, text, image, favorite):
    self.text = text
    self.image = image
    self.favorite = favorite

class MemeSchema(ma.Schema):
  class Meta:
    fields = ("id", "text", "image", "favorite")

meme_schema = MemeSchema()
memes_schema = MemeSchema(many=True)

if __name__ == "__main__":
  app.debug = True
  app.run()