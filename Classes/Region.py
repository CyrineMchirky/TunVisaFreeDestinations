from db import db 

class RegionModel(db.Model): 

    __tablename__='regions'  

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(80))   
    
    
    destinations = db.relationship('DestinationModel', lazy='dynamic') 

    def __init__(self, name):
        self.name=name
        


    def json(self):
        return{'name':self.name, 'destinations': [destination.json() for destination in self.destinations.all()]}

    @classmethod
    def find_by_name(self, name):
        return self.query.filter_by(name=name).first() 


    
    def save_to_db(self): 
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self): 
        db.session.delete(self)
        db.session.commit()