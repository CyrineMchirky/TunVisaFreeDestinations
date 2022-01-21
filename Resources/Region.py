from flask_restful import Resource
from Classes.Region import RegionModel

class Region(Resource):
    
    def get(self, name):
        region = RegionModel.find_by_name(name)
        if region:
            return region.json()
        return {'message': 'Write the correct Region name'}, 404
        
    def post(self, name):
        if RegionModel.find_by_name(name):
            return {'message': "This Region '{}' is already added.".format(name)}, 400

        region = RegionModel(name)
        try:
            region.save_to_db()
        except:
            return {"message": "An error occurred adding the region."}, 500

        return region.json(), 201
    
    def delete(self, name):
        region = RegionModel.find_by_name(name)
        if region:
            region.delete_from_db()

        return {'message': 'Region was deleted'}
        
    
class RegionList(Resource):
    def get(self):
        return {'Regions': list(map(lambda x: x.json(), RegionModel.query.all()))}   