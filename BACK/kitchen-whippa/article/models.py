# articles/models.py

from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    ingredients = db.Column(db.JSON)
    steps = db.Column(db.JSON)
    has_image = db.Column(db.Boolean)
    labels = db.Column(db.JSON)
    category = db.Column(db.String(50))
    creation_date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Article {self.title}>'
