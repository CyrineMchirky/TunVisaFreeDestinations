from flask import Flask
from flask_restful import Api


def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'Cyrina is trying her best'
    api = Api(app) 
    return app

app = create_app()
if __name__ == '__main__' : 
    app.run(debug=True)