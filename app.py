from charset_normalizer import api
from flask import Flask, app
from flask_restful import Api
from flask import Flask
from flask_jwt import JWT
from Security import authenticate, identity
from Resources.user import UserRegister
from Resources.Destination import Destination, DestinationList
from Resources.Region import Region, RegionList
from db import db
import os
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:theWebService99@db.emvjzikhqhijkhgmpciw.supabase.co:6543/postgres' #'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.secret_key = 'Cyrina is trying her best'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)


api.add_resource(Region, '/region/<string:name>')
api.add_resource(Destination, '/destination/<string:name>')
api.add_resource(DestinationList, '/destinations')
api.add_resource(RegionList, '/regions')
api.add_resource(UserRegister, '/register')



from db import db
db.init_app(app)  

if os.getenv("ENV_CONFIG") != "production":
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')  
