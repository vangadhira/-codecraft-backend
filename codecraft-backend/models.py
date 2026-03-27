from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    total_points = db.Column(db.Integer, default=0)

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    difficulty = db.Column(db.String(50))
    points = db.Column(db.Integer)

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    challenge_id = db.Column(db.Integer)
    completed = db.Column(db.Boolean, default=False)
    hints_used = db.Column(db.Integer, default=0)
    used_explanation = db.Column(db.Boolean, default=False)
    points_earned = db.Column(db.Integer)