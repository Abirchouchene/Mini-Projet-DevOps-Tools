from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

USER_SERVICE_URL = "http://user-service:5001"
SALLE_SERVICE_URL = "http://salle-service:5002"
RESERVATION_SERVICE_URL = "http://reservation-service:5003"

@app.route('/auth/<path:path>', methods=['GET'])
def auth_proxy(path):
    return requests.get(f"{USER_SERVICE_URL}/auth/{path}", params=request.args).json()

@app.route('/users', methods=['GET', 'POST'])
def users_proxy():
    if request.method == 'GET':
        return requests.get(f"{USER_SERVICE_URL}/users", headers=request.headers).json()
    else:
        return requests.post(f"{USER_SERVICE_URL}/users", json=request.get_json(), headers=request.headers).json()

@app.route('/salles', methods=['GET', 'POST'])
def salles_proxy():
    if request.method == 'GET':
        return requests.get(f"{SALLE_SERVICE_URL}/salles", headers=request.headers).json()
    else:
        return requests.post(f"{SALLE_SERVICE_URL}/salles", json=request.get_json(), headers=request.headers).json()

@app.route('/reservations', methods=['GET', 'POST'])
def reservations_proxy():
    if request.method == 'GET':
        return requests.get(f"{RESERVATION_SERVICE_URL}/reservations", headers=request.headers).json()
    else:
        return requests.post(f"{RESERVATION_SERVICE_URL}/reservations", json=request.get_json(), headers=request.headers).json()

@app.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def reservation_delete_proxy(reservation_id):
    return requests.delete(f"{RESERVATION_SERVICE_URL}/reservations/{reservation_id}", headers=request.headers).json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)