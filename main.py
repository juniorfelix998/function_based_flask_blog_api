import os
import logging


from dotenv import load_dotenv

from flask import Flask, jsonify

from core.database import db
from core.utils.responses import response_with
import core.utils.responses as resp
from core.config import DevelopmentConfig, ProductionConfig, TestingConfig
from posts.routes import post_routes

load_dotenv('.env')


def parse_config(app):
    env = os.environ.get('ENV')
    if env == "DEV":
        app.config.from_object(DevelopmentConfig)
        app.logger.debug(" * ENV: DEVELOPMENT")
    if env == "PROD":
        app.config.from_object(ProductionConfig)
        app.logger.debug(" * ENV: PRODUCTION")
    if env == "TEST":
        app.config.from_object(TestingConfig)
        app.logger.debug(" * ENV: TESTING")


def create_app():
    app = Flask(__name__)
    parse_config(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(post_routes, url_prefix='/api/posts')

    # START GLOBAL HTTP CONFIGURATIONS
    @app.after_request
    def add_header(response):
        return response

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

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


app = create_app()
