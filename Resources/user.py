from flask_restful import Resource, reqparse

import os,sys
dir_path=os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, 
os.pardir))
sys.path.insert(0, parent_dir_path)

from Classes.user import UserModel

        
class UserRegister(Resource):
    TABLE_NAME='users'
    
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required= True, help="Please enter your username")
    parser.add_argument('password', type=str, required= True, help="Please enter your password")
    
    def post(self):
        data=UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return{"message": "This Username already exists."}, 400
     
        user = UserModel(**data) 
        user.save_to_db()
        
        return{"message": "User created successfully."}, 201