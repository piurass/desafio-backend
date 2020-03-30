from setup 		import constants
from flask 		import Flask, request, jsonify, abort
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = constants.JWT_SECRET_KEY
jwt = JWTManager(app)

@app.route("/")
def index():
    return "Tembici Ckeck!"

@app.route(constants.ROUTE_CHECK, methods = ['GET'])
@jwt_required
def check():
    current_user = get_jwt_identity()
    return jsonify(usuario=current_user)

if __name__ == '__main__':
    app.run(debug=True, port=constants.PORT_CHECK)
