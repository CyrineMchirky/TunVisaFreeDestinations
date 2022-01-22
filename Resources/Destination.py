from tokenize import String
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

import os,sys

from sqlalchemy import Integer
dir_path=os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path,
os.pardir))
sys.path.insert(0, parent_dir_path)

from Classes.Destination import DestinationModel

class Destination(Resource):
    parser = reqparse.RequestParser()
    

    
    parser.add_argument('region_id',
        type=int,
        required=True,
        help="This field cannot be left blank! Please enter the region id for this destination."
    )
    
    parser.add_argument('Visa_requirement',
        type=String,
        required=True,
        help="This field cannot be left blank! Enter Visa requirements for this destination."
    )
    parser.add_argument('Allowed_stay',
        type=String,
        required=True,
        help="This field cannot be left blank! Enter how many days are allowed to stay without a visa in this destination."
    )
    parser.add_argument('budget',
        type=String,
        required=True,
        help="This field cannot be left blank!Add the budget per day for this destination."
    )
    parser.add_argument('vaccines',
        type=String,
        required=True,
        help="This field cannot be left blank! Enter the vaccines needed to access this destination."
    )
    parser.add_argument('airport',
        type=String,
        required=True,
        help="This field cannot be left blank! Enter the landing airport destination."
    )

    parser.add_argument('price',
        type=Integer,
        required=True,
        help="This field cannot be left blank! Enter airplane ticket price for this destination."
    )
    parser.add_argument('time_of_flight',
        type=String,
        required=True,
        help="This field cannot be left blank! Enter the flight time for this destination."
    )

    @jwt_required()
    def get(self, name):
        destination=DestinationModel.find_by_name(name)
        if destination:
            return destination.json()
        return{'message': 'Destination is not found or you misspelled it'}, 404



    def post(self, name):
        destination=DestinationModel.find_by_name(name)
        if DestinationModel.find_by_name(name):
            return {'message': "This destination '{}' is already added.".format(name)}

        data = destination.parser.parse_args()
        
        
        destination  = DestinationModel(name, **data)
        
        try:
            destination.save_to_db()
        except:
            return{"message": "An error occured when adding the destination"}, 500 

        return destination.json(), 201



    @jwt_required()
    def delete(self, name):

        destination = DestinationModel.find_by_name(name) 
        if destination:
            destination.delete_from_db()
            return {'message': 'Destination deleted'}
        return {'message': 'Destination not found.'}, 404

    @jwt_required()
    def put(self, name):
        
        
        destination = DestinationModel.find_by_name(name)
        data = destination.parser.parse_args()
        if destination is None:
            
            destination = DestinationModel(name, **data)
        else:
            destination.Visa_requirements = data['Visa_requirements']
            destination.Allowed_stay = data['Allowed_stay']
            destination.budget = data['budget']
            destination.vaccines = data['vaccines']
            destination.airport = data['airport']
            destination.price = data['price']
            destination.time_of_flight = data['time_of_flight']

        destination.save_to_db()
        return destination.json()




class DestinationList(Resource):
    def get(self):
     return {'destinations': [x.json() for x in DestinationModel.query.all()]}