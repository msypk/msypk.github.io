import flask
from application import db

class Experience(db.Document):
    job_id = db.IntField(unique=True)
    company = db.StringField(max_length=50)
    role = db.StringField(max_length=100)
    period = db.StringField(max_length=50)
    location = db.StringField(max_length=100)
    summary = db.StringField(max_length=500)
    achievement = db.StringField(max_length=250)
    

class Post(db.Document):
    post_id = db.IntField(unique=True)
    title = db.StringField(max_length=50)
    teaser = db.StringField(max_length=500)
    body = db.ListField()
    date = db.DateTimeField()
    heading = db.ListField()
    image_description = db.StringField(max_length=50)

