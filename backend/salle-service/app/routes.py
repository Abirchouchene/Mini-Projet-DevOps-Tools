from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import Salle
from . import db
from .utils import check_availability, update_availability

bp = Blueprint('routes', __name__)

@bp.route('/salles', methods=['GET'])
@jwt_required()
def get_salles():
    salles = Salle.query.all()
    return jsonify([{"id": salle.id, "name": salle.name, "capacity": salle.capacity, "available": salle.available} for salle in salles])

@bp.route('/salles', methods=['POST'])
@jwt_required()
def create_salle():
    current_user = get_jwt_identity()
    if current_user['role'] not in ["Admin", "Employé"]:
        return jsonify({"message": "Accès non autorisé"}), 403
    data = request.get_json()
    salle = Salle(name=data['name'], capacity=data['capacity'])
    db.session.add(salle)
    db.session.commit()
    return jsonify({"message": "Salle créée", "name": salle.name}), 201

@bp.route('/salles/<int:salle_id>/availability', methods=['GET'])
@jwt_required()
def get_availability(salle_id):
    available = check_availability(salle_id)
    return jsonify({"salle_id": salle_id, "available": available})

@bp.route('/salles/<int:salle_id>/availability', methods=['PUT'])
@jwt_required()
def set_availability(salle_id):
    data = request.get_json()
    update_availability(salle_id, data['available'])
    return jsonify({"message": "Disponibilité mise à jour"})