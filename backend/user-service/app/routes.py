from flask import Blueprint, request, jsonify
from app import db
from app.models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(email=data["email"], name=data["name"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])
