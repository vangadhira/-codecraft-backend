from flask import Flask
from flask_cors import CORS
from models import db
from flask_jwt_extended import JWTManager

from routes.auth import auth_routes
from routes.challenge import challenge_routes
from routes.dashboard import dashboard

app = Flask(__name__)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///codecraft.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db.init_app(app)
jwt = JWTManager(app)

CORS(app)

# ROUTES
app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(challenge_routes, url_prefix='/challenge')
app.register_blueprint(dashboard, url_prefix='/dashboard')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)