from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    #def __repr__(self):
        #return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    type = db.Column(db.String(100), unique=False, nullable=False)
    second_type = db.Column(db.String(100), unique=False, nullable=True) 
    height = db.Column(db.String(100), unique=False, nullable=False)
    weight = db.Column(db.String(100), unique=False, nullable=False)
    primary_ability = db.Column(db.String(100), unique=False, nullable=False)
    secondary_ability = db.Column(db.String(100), unique=False, nullable=True)
    hidden_ability = db.Column(db.String(100), unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name, 
            "type": self.type,
            "second_type": self.second_type, 
            "height": self.height,
            "weight": self.weight,
            "primary_ability": self.primary_ability,
            "secondary_ability": self.secondary_ability,
            "hidden_ability": self.hidden_ability,
        }

class Region(db.Model):
    __tablename__ = "region"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    number_of_cities = db.Column(db.String(10), unique=False, nullable=False)
    professor = db.Column(db.String(100), unique=False, nullable=False)
    initials_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    initials = db.relationship(Pokemon, uselist=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name, 
            "number_of_cities": self.number_of_cities,
            "professor": self.professor,
            "initials_id": self.initials.name,
        }
  
class Cities(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    gym_leader = db.Column(db.String(100), unique=True, nullable=False)
    city_region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    city_region = db.relationship(Region, uselist=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gym_leader": self.gym_leader, 
            "city_region_id": self.city_region.name
        }

class Favourites(db.Model):
    __tablename__ = "favourites"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    person = db.relationship(User, uselist=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))
    favourite_pokemon = db.relationship(Pokemon, uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "person_id": self.person.name, 
            "pokemon_id": self.favourite_pokemon.name,
        }