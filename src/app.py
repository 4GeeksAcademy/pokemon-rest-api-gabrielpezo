"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Pokemon, Region, Cities, Favourites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_get_all_users():
    handle_get_all_users = User().query.all()
    get_all_users = list(map(lambda user:user.serialize(), handle_get_all_users))
    return jsonify({"data": get_all_users}), 200

@app.route('/user/<int:id>', methods=['GET'])
def handle_get_user(id):
    get_user = User.query.get_or_404(id)  
    return jsonify(get_user.serialize()), 200

@app.route('/pokemons', methods=['GET'])
def handle_get_all_pokemons():
    handle_get_all_pokemons = Pokemon().query.all()
    get_all_pokemons = list(map(lambda pokemon:pokemon.serialize(), handle_get_all_pokemons))
    return jsonify({"data": get_all_pokemons}), 200

@app.route('/pokemons/<int:id>', methods=['GET'])
def handle_get_pokemon(id):
    get_pokemon = Pokemon.query.get_or_404(id)  
    return jsonify(get_pokemon.serialize()), 200


@app.route('/regions', methods=['GET'])
def handle_get_all_regions():
    handle_get_all_regions = Region().query.all()
    get_all_regions = list(map(lambda region:region.serialize(), handle_get_all_regions))
    return jsonify({"data": get_all_regions}), 200

@app.route('/regions/<int:id>', methods=['GET'])
def handle_get_region(id):
    get_region = Region.query.get_or_404(id)  
    return jsonify(get_region.serialize()), 200

@app.route('/cities', methods=['GET'])
def handle_get_all_cities():
    handle_get_all_cities = Cities().query.all()
    get_all_cities = list(map(lambda city:city.serialize(), handle_get_all_cities))
    return jsonify({"data": get_all_cities}), 200

@app.route('/cities/<int:id>', methods=['GET'])
def handle_get_city(id):
    get_city = Cities.query.get_or_404(id)  
    return jsonify(get_city.serialize()), 200

@app.route('/favourites', methods=['GET'])
def handle_get_all_favourites():
    handle_get_all_favourites = Favourites().query.all()
    get_all_favourites = list(map(lambda city:city.serialize(), handle_get_all_favourites))
    return jsonify({"data": get_all_favourites}), 200

@app.route('/favourites/<int:id>', methods=['GET'])
def handle_get_favourites(id):
    get_favourite = Favourites.query.get_or_404(id)  
    return jsonify(get_favourite.serialize()), 200



@app.route('/create', methods=['POST'])
def handle_user():
    data = request.get_json()
    create_region = User()
    create_region.name = data["name"]
    create_region.email = data["email"]
    create_region.password = data["password"]
    create_region.is_active = data["active"]

    db.session.add(create_region)
    db.session.commit()

    return jsonify({"data": data}), 200

@app.route('/pokemon', methods=['POST'])
def handle_pokemon():
    data = request.get_json()
    create_pokemon = Pokemon()
    create_pokemon.name = data["name"]
    create_pokemon.type = data["type"]
    create_pokemon.second_type = data["second_type"]
    create_pokemon.height = data["height"]
    create_pokemon.weight = data["weight"]
    create_pokemon.primary_ability = data["primary_ability"]
    create_pokemon.secondary_ability = data["secondary_ability"]
    create_pokemon.hidden_ability = data["hidden_ability"]

    db.session.add(create_pokemon)
    db.session.commit()

    return jsonify({"data": data}), 200

@app.route('/create_regions', methods=['POST'])
def handle_region():
    data = request.get_json()
    create_region = Region()
    create_region.name = data["name"]
    create_region.number_of_cities = data["number_of_cities"]
    create_region.professor = data["professor"]
    create_region.initials_id = data["initials_id"]

    db.session.add(create_region)
    db.session.commit()

    return jsonify({"data": data}), 200

@app.route('/create_city', methods=['POST'])
def handle_city():
    data = request.get_json()
    create_city = Cities()
    create_city.name = data["name"]
    create_city.gym_leader = data["gym_leader"]
    create_city.city_region_id = data ["city_region_id"]

    db.session.add(create_city)
    db.session.commit()

    return jsonify({"data": data}), 200

@app.route('/create_favourite', methods=['POST'])
def handle_favourites():
    data = request.get_json()
    create_favourites = Favourites()
    create_favourites.person_id = data["person_id"]
    create_favourites.pokemon_id = data["pokemon_id"]

    db.session.add(create_favourites)
    db.session.commit()

    return jsonify({"data": data}), 200



@app.route('/user/<int:id>', methods=['PUT'])
def handle_update_user(id):
    update_user = User.query.get_or_404(id)
    data = request.get_json()
    if "name" in data:
        update_user.name = data["name"]
    if "email" in data:
        update_user.email = data["email"]
    if "password" in data:
        update_user.password = data["password"]

    db.session.commit()
    return jsonify(update_user.serialize()), 200

@app.route('/pokemons/<int:id>', methods=['PUT'])
def handle_update_pokemon(id):
    update_pokemon = Pokemon.query.get_or_404(id)
    data = request.get_json()
    if "name" in data:
        update_pokemon.name = data["name"]
    if "type" in data:
        update_pokemon.type = data["type"]
    if "second_type" in data:
        update_pokemon.second_type = data["second_type"]
    if "height" in data:
        update_pokemon.height = data["height"]
    if "weight" in data:
        update_pokemon.weight = data["weight"]
    if "primary_ability" in data:
        update_pokemon.primary_ability = data["primary_ability"]
    if "secondary_ability" in data:
        update_pokemon.secondary_ability = data["secondary_ability"]
    if "hidden_ability" in data:
        update_pokemon.hidden_ability = data["hidden_ability"]

    db.session.commit()
    return jsonify(update_pokemon.serialize()), 200

@app.route('/regions/<int:id>', methods=['PUT'])
def handle_update_region(id):
    update_region = Region.query.get_or_404(id)
    data = request.get_json()
    if "name" in data:
        update_region.name = data["name"]
    if "number_of_cities" in data:
        update_region.number_of_cities = data["number_of_cities"]
    if "professor" in data:
        update_region.professor = data["professor"]

    db.session.commit()
    return jsonify(update_region.serialize()), 200

@app.route('/cities/<int:id>', methods=['PUT'])
def handle_update_city(id):
    update_city = Cities.query.get_or_404(id)
    data = request.get_json()
    if "name" in data:
        update_city.name = data["name"]
    if "gym_leader" in data:
        update_city.gym_leader = data["gym_leader"]

    db.session.commit()
    return jsonify(update_city.serialize()), 200

@app.route('/favourites/<int:id>', methods=['PUT'])
def handle_update_favourites(id):
    update_favourites = Favourites.query.get_or_404(id)
    data = request.get_json()
    if "pokemon_id" in data:
        update_favourites.pokemon_id = data["pokemon_id"]

    db.session.commit()
    return jsonify(update_favourites.serialize()), 200



@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    get_user = User.query.get_or_404(id)
    db.session.delete(get_user)
    db.session.commit()
    return jsonify({"msg": "User was deleted"}), 200

@app.route('/pokemons/<int:id>', methods=['DELETE'])
def delete_pokemon(id):
    get_pokemon = Pokemon.query.get_or_404(id)
    db.session.delete(get_pokemon)
    db.session.commit()
    return jsonify({"msg": "Pokemon was deleted"}), 200

@app.route('/regions/<int:id>', methods=['DELETE'])
def delete_region(id):
    get_region = Region.query.get_or_404(id)
    db.session.delete(get_region)
    db.session.commit()
    return jsonify({"msg": "Region was deleted"}), 200

@app.route('/cities/<int:id>', methods=['DELETE'])
def delete_city(id):
    get_city = Cities.query.get_or_404(id)
    db.session.delete(get_city)
    db.session.commit()
    return jsonify({"msg": "City was deleted"}), 200

@app.route('/favourites/<int:id>', methods=['DELETE'])
def delete_favourites(id):
    get_favourites = Favourites.query.get_or_404(id)
    db.session.delete(get_favourites)
    db.session.commit()
    return jsonify({"msg": "Favourite elements were deleted"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
