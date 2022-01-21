from db import db 

class DestinationModel(db.Model): 

    __tablename__='destinations'  

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))  
    Visa_requirements = db.Column(db.String(60))  
    Allowed_stay = db.Column(db.String(80)) 
    budget = db.Column(db.String(80)) 
    vaccines = db.Column(db.String(150)) 
    airport = db.Column(db.String(100)) 
    price = db.Column(db.Integer) 
    time_of_flight = db.Column(db.String(80)) 

    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    region = db.relationship('RegionModel')

    def __init__(self, name,Visa_requirements,Allowed_stay,budget,vaccines,airport, price,time_of_flight, region_id):
        self.name=name
        self.Visa_requirements=Visa_requirements
        self.Allowed_stay=Allowed_stay
        self.budget=budget
        self.vaccines=vaccines
        self.airport=airport
        self.price=price
        self.time_of_flight=time_of_flight
        self.region_id=region_id

    def json(self):
        return{'name':self.name, 'Visa_Requirement':self.Visa_requirements,
        'Allowed_Stay':self.Allowed_stay, 'budget':self.budget,
        'vaccines':self.vaccines, 'Airport':self.airport,
        'price':self.price, 'time_of_flight':self.time_of_flight}


    @classmethod
    def find_by_name(self, name):
        return self.query.filter_by(name=name).first() 
    
    
    def save_to_db(self): 
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self): 
        db.session.delete(self)
        db.session.commit()
