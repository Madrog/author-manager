import logging
import os
import sys
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.utils import send_from_directory


def create_app(config):    
    app = Flask(__name__)
    app.config.from_object(config)

    from api.utils.database import db
    db.init_app(app)
       
    from api.utils.email import mail
    mail.init_app(app)

    from api.routes.authors import author_routes
    app.register_blueprint(author_routes, url_prefix='/api/authors')

    from api.routes.books import book_routes
    app.register_blueprint(book_routes, url_prefix='/api/books')

    from api.routes.users import user_routes 
    app.register_blueprint(user_routes, url_prefix='/api/users')

    @app.route('/avatar/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    from api.utils.responses import response_with
    import api.utils.responses as resp

    # START GLOBAL HTTP CONFIGURATIONS
    @app.after_request
    def add_header(response):
        return response


    @app.route("/api/spec")
    def spec():
        swag = swagger(app, prefix='/api')
        swag['info']['base'] = "http://localhost:5000"
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Flask Author DB"
        return jsonify(swag)



    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)


    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)


    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_404)

    # END GLOBAL HTTP CONFIGURATIONS

    jwt = JWTManager(app)
    
    logging.basicConfig(stream=sys.stdout,
                        format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
                        level=logging.DEBUG)
    
    return app


