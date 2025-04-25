from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

bp = Blueprint('routes', __name__)

@bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    return jsonify({"users": []})

@bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Exemple simple : vérifie un utilisateur (remplace par une vraie logique d'authentification)
    if username == "admin" and password == "password":  # À remplacer par une vérification en base de données
        access_token = create_access_token(identity={"username": username, "role": "Admin"})
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@bp.route('/auth/login', methods=['GET'])
def check_login():
    # Vérifie si un utilisateur est connecté (avec un token JWT)
    try:
        current_user = get_jwt_identity()
        if current_user:
            return jsonify({"message": "User is logged in", "user": current_user}), 200
    except:
        pass
    return jsonify({"message": "User is not logged in"}), 401