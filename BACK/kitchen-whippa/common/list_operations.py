# common/list_operations.py

from app import db
from common.models import ImageList, CommentList
from article.models import Article
from comments.models import Comment

def get_image_list(article_id):
    # Lógica para obtener la lista de imágenes relacionadas con un artículo
    # (Implementa según tus necesidades)
    return ImageList.query.filter_by(article_id=article_id).all()

def get_comment_list(article_id):
    # Lógica para obtener la lista de comentarios relacionados con un artículo
    # (Implementa según tus necesidades)
    return CommentList.query.filter_by(article_id=article_id).all()
