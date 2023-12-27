# comments/models.py

from app import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    article_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Comment {self.id}>'
