from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.authors import Author, AuthorSchema
from api.utils.database import db

author_routes = Blueprint("author_routes", __name__)

@author_routes.route('/', methods=['POST'])
def create_author():
    try:
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400
        # Validate and deserialize input
        author_schema = AuthorSchema()
        try:
            data = author_schema.load(json_data)
        except Exception as e:
            print(e)
            return {"message": "Validation Error occurred."}, 400
        author = Author(first_name=data["first_name"], last_name=data["last_name"])
        result = author_schema.dump(author.create())
        return response_with(resp.SUCCESS_201, value={"author": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@author_routes.route('/', methods=['GET'])
def get_author_list():
    fetched = Author.query.all() 
    author_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])
    authors = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"authors": authors})


@author_routes.route('/<int:author_id>', methods=['GET'])
def get_author_detail(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"author": author})

