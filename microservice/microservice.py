from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager


"""app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:supersecure@db/rest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:supersecure@db/rest'"""



database = SQLAlchemy()


def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:supersecure@db/rest'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(app)
    database.create_all()
    app.app_context().push()
    return app


def create_production_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:supersecure@db/rest'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(app)
    app.app_context().push()
    return app

app = create_production_app()


@app.before_first_request
def create_db():
    database.create_all()


class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column('username', database.String(20), unique=True, index=True)
    password = database.Column('password', database.String(41))

    def __init__(self, username, password):
        self.username = username
        self.password = password


manager = APIManager(app, flask_sqlalchemy_db=database)
manager.create_api(User, methods=['GET', 'POST', 'DELETE', 'PUT'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
