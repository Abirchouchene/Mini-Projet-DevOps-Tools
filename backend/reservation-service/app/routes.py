from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

bp = Blueprint('routes', __name__)

@bp.route('/reservations', methods=['GET'])
@jwt_required()
def get_reservations():
    return jsonify({"reservations": []})