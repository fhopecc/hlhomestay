import datetime
from google.appengine.ext import db
from google.appengine.api import users
class Homestay(db.Model):
  name  = db.StringProperty(required=True)
  link = db.LinkProperty(required=True)
  email = db.EmailProperty(required=True)
  status = db.StringProperty(required=True, choices=set(["valid",
    "invalid"]))
  create_at = db.DateProperty()
