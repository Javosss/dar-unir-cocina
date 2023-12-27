# common/routes.py

from flask import jsonify
from app import app
from common.list_operations import get_image_list, get_comment_list

@app.route('/image-list-retrieve/<int:id_article>', methods=['POST'])
def retrieve_image_list(id_article):
    image_list = get_image_list(id_article)
    # Puedes personalizar la respuesta según tus necesidades
    return jsonify({'image_list': image_list}), 200

@app.route('/comment-list/<int:id_article>', methods=['POST'])
def retrieve_comment_list(id_article):
    comment_list = get_comment_list(id_article)
    # Puedes personalizar la respuesta según tus necesidades
    return jsonify({'comment_list': comment_list}), 200
