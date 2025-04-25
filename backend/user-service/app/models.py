from flask import Blueprint, redirect, request, jsonify
from flask_jwt_extended import create_access_token
import requests
from .models import User
from . import db

auth_bp = Blueprint('auth', __name__)

GOOGLE_CLIENT_ID = "your-google-client-id"
GOOGLE_CLIENT_SECRET = "your-google-client-secret"
GOOGLE_REDIRECT_URI = "http://localhost:5000/auth/callback"

@auth_bp.route('/login')
def login():
    google_auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&response_type=code&scope=email profile"
    return redirect(google_auth_url)

@auth_bp.route('/callback')
def callback():
    code = request.args.get('code')
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    response = requests.post(token_url, data=data)
    token = response.json().get("access_token")
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {token}"}).json()
    
    email = user_info.get("email")
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email, role="Visiteur")
        db.session.add(user)
        db.session.commit()
    
    access_token = create_access_token(identity={"email": email, "role": user.role})
    return jsonify({"message": "Authentification réussie", "access_token": access_token, "user": user_info})