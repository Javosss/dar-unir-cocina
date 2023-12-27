# comments/routes.py

from flask import request, jsonify
from app import app, db
from comments.models import Comment

@app.route('/comment/<int:id_article>/<int:id_user>', methods=['PUT'])
def update_comment(id_article, id_user):
    data = request.get_json()
    comment = Comment.query.filter_by(article_id=id_article, user_id=id_user).first_or_404()

    # Actualizar propiedades del comentario según sea necesario
    comment.content = data['content']

    db.session.commit()

    return jsonify({'message': 'Comment updated successfully'}), 200

@app.route('/comment/<int:id_article>/<int:id_user>', methods=['POST'])
def add_comment(id_article, id_user):
    data = request.get_json()
    new_comment = Comment(user_id=id_user, article_id=id_article, content=data['content'])

    db.session.add(new_comment)
    db.session.commit()

    return jsonify({'message': 'Comment created successfully'}), 201

@app.route('/comment/<int:id_article>/<int:id_user>', methods=['DELETE'])
def delete_comment(id_article, id_user):
    comment = Comment.query.filter_by(article_id=id_article, user_id=id_user).first_or_404()

    db.session.delete(comment)
    db.session.commit()

    return jsonify({'message': 'Comment deleted successfully'}), 200
