from setup 		import constants
from flask 		import Flask, request, jsonify, abort
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = constants.JWT_SECRET_KEY
jwt = JWTManager(app)

@app.route("/")
def index():
    return "Tembici Login!"

@app.route(constants.ROUTE_LOGIN, methods = ['POST'])
def login():
    if not request.json:
        abort(400)
    usuario 	= request.json['usuario']
    senha 	= request.json['senha']

    access_token = create_access_token(identity=usuario)
    return jsonify(access_token=access_token), 200

if __name__ == '__main__':
    app.run(debug=True, port=constants.PORT_LOGIN)
