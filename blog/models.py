# author:Sole_idol
# filename: models.py
# datetime:2020/8/22 9:38
from libs.orm import db
from datetime import datetime


class BlogText(db.Model):
    __tablename__ = 'blog_text'
    
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(40))
    content = db.Column(db.Text, nullable=False)
    up_time = db.Column(db.Date, default=datetime.now())
