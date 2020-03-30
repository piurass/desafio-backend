from setup 		import constants
from model.viagem 	import Viagem
from flask 		import Flask, request, jsonify, abort
from flask_jwt_extended	import JWTManager, jwt_required, create_access_token, get_jwt_identity
import peewee

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = constants.JWT_SECRET_KEY
jwt = JWTManager(app)

@app.route("/")
def index():
    return "Tembici Viagem!"

@app.route(constants.ROUTE_VIAGEM, methods = ['GET'])
@jwt_required
def check():
    current_user = get_jwt_identity()

    try:
        viagens	= Viagem.get(Viagem.user==current_user)
        data	= Viagem.modelToJson(viagens)
        return jsonify(data)
    except peewee.OperationalError:
        return jsonify(ret='')

@app.route(constants.ROUTE_VIAGEM, methods = ['POST'])
@jwt_required
def score():
    if not request.json:
        abort(400)

    try:
        data	= Viagem.requestToJson(request, get_jwt_identity())
        viagem	= Viagem.insert(data)
        return jsonify(ret=True)
    except peewee.OperationalError:
        return jsonify(ret=False)

if __name__ == '__main__':
    app.run(debug=True, port=constants.PORT_VIAGEM)
