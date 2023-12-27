# tags/routes.py

from flask import request, jsonify
from app import app, db
from tags.models import Tag

@app.route('/tag/<int:id_article>', methods=['PUT'])
def add_tag(id_article):
    data = request.get_json()
    new_tag = Tag(name=data['name'])
    db.session.add(new_tag)
    db.session.commit()
    return jsonify({'message': 'Tag created successfully'}), 201

@app.route('/tag/<int:id_tag>', methods=['DELETE'])
def delete_tag(id_tag):
    tag = Tag.query.get_or_404(id_tag)
    db.session.delete(tag)
    db.session.commit()
    return jsonify({'message': 'Tag deleted successfully'}), 200

@app.route('/tag/<int:id_tag>', methods=['POST'])
def update_tag(id_tag):
    tag = Tag.query.get_or_404(id_tag)
    data = request.get_json()
    tag.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Tag updated successfully'}), 200
