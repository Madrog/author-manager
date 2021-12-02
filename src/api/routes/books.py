from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.books import Book, BookSchema
from api.utils.database import db

book_routes = Blueprint("book_routes", __name__)

@book_routes.route('/', methods=['POST'])
@jwt_required()
def create_book():
    try:
        json_data = request.get_json()       
        # Validate and deserialize input
        book_schema = BookSchema()
        data = book_schema.load(json_data)

        title = data['title']
        year = int(data['year']) 
        author_id = int(data['author_id'])
        
        book = Book(title=title, year=year, author_id=author_id)
        result = book_schema.dump(book.create())
        return response_with(resp.SUCCESS_201, value={"book": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_FIELDS_NAME_SENT_422)


@book_routes.route('/', methods=['GET'])
def get_book_list():
    fetched = Book.query.all()
    book_schema = BookSchema(many=True, only=['author_id', 'title', 'year'])
    books = book_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"books": books})


@book_routes.route('/<int:id>', methods=['GET'])
def get_book_detail(id):
    fetched = Book.query.get_or_404(id)
    book_schema = BookSchema()
    books = book_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"books": books})


@book_routes.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_book_detail(id):
    data = request.get_json()
    get_book = Book.query.get_or_404(id)
    get_book.title = data['title']
    get_book.year = data['year']
    db.session.add(get_book)
    db.session.commit()
    book_schema = BookSchema()
    book = book_schema.dump(get_book)
    return response_with(resp.SUCCESS_200, value={"book": book})


@book_routes.route('/<int:id>', methods=['PATCH'])
@jwt_required()
def modify_book_detail(id):
    data = request.get_json()
    get_book = Book.query.get_or_404(id)
    if data.get('title'):
        get_book.title = data['title']
    if data.get('year'):
        get_book.year = data['year']
    db.session.add(get_book)
    db.session.commit()
    book_schema = BookSchema()
    book = book_schema.dump(get_book)
    return response_with(resp.SUCCESS_200, value={"book": book})


@book_routes.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    get_book = Book.query.get_or_404(id)
    db.session.delete(get_book)
    db.session.commit()
    return response_with(resp.SUCCESS_204)