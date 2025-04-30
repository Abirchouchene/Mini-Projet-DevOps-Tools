import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:Nothing123@localhost:5432/reservation_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False