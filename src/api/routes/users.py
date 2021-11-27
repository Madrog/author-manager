from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.users import User, UserSchema
from api.utils.database import db
from flask_jwt_extended import create_access_token

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/', methods=['POST'])
def create_user():
    try:
        json_data = request.get_json()
        json_data['password'] = User.generate_hash(json_data['password'])
        user_schema = UserSchema()
        data = user_schema.load(json_data)
        user = User(username=data['username'], password=data['password'])
        result = user_schema.dump(user.create())
        return response_with(resp.SUCCESS_201)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_FIELDS_NAME_SENT_422)


@user_routes.route('/login', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        current_user = User.find_by_username(data['username'])
        if not current_user:
            return response_with(resp.SERVER_ERROR_404)
        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            return response_with(resp.SUCCESS_201, value={'message': 'Logged in {}'.format(current_user.username), 
                                    "access_token": access_token})
        else:
            return response_with(resp.UNAUTHORIZED_401)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


