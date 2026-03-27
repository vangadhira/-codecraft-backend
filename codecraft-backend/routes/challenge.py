from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered"})


@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(
        email=data.get('email'),
        password=data.get('password')
    ).first()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)

    return jsonify({
        "token": token,
        "user_id": user.id
    })