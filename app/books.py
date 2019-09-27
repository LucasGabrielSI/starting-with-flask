from .model import Book
from .serializer import BookSchema
from marshmallow import ValidationError
from flask import Blueprint, current_app, request, jsonify

bp_books = Blueprint('books', __name__)


@bp_books.route('/insert', methods=['POST'])
def insert():
    bs = BookSchema()
    try:
        book = bs.load(request.json)
        current_app.db.session.add(book)
        current_app.db.session.commit()
        return bs.jsonify(book), 201
    except ValidationError:
        return 'An error has occurred'


@bp_books.route('/display', methods=['GET'])
def display():
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200


@bp_books.route('/update/<id>', methods=['POST'])
def update(id):
    bs = BookSchema()
    query = Book.query.filter(Book.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())


@bp_books.route('/delete/<id>', methods=['GET'])
def delete(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
    return jsonify('BOOOW')
