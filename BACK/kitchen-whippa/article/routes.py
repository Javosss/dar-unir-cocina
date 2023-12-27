# articles/routes.py

from flask import request, jsonify
from app import app, db
from articles.models import Article

@app.route('/article', methods=['PUT'])
def add_article():
    data = request.get_json()
    new_article = Article(
        title=data['title'],
        description=data.get('description'),
        ingredients=data.get('ingredients'),
        steps=data.get('steps'),
        has_image=data.get('has_image'),
        labels=data.get('labels'),
        category=data.get('category')
    )

    db.session.add(new_article)
    db.session.commit()

    return jsonify({'message': 'Article created successfully'}), 201

@app.route('/article/<int:id_article>', methods=['DELETE'])
def delete_article(id_article):
    article = Article.query.get_or_404(id_article)

    db.session.delete(article)
    db.session.commit()

    return jsonify({'message': 'Article deleted successfully'}), 200

@app.route('/article/<int:id_article>', methods=['POST'])
def update_article(id_article):
    article = Article.query.get_or_404(id_article)
    data = request.get_json()

    # Actualizar propiedades del artículo según sea necesario
    article.title = data['title']
    article.description = data.get('description')
    article.ingredients = data.get('ingredients')
    article.steps = data.get('steps')
    article.has_image = data.get('has_image')
    article.labels = data.get('labels')
    article.category = data.get('category')

    db.session.commit()

    return jsonify({'message': 'Article updated successfully'}), 200
