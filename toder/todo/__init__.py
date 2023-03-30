import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_HOST_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_HOST_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    from . import db

    db.init_app(app)

    @app.route('/hola')
    def hola():
        return 'chanchito feliz'

    return app