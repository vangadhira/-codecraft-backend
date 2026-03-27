from flask import Blueprint, jsonify
from models import User, UserProgress

dashboard = Blueprint('dashboard', __name__)

# 🏆 Leaderboard
@dashboard.route('/leaderboard', methods=['GET'])
def leaderboard():
    users = User.query.order_by(User.total_points.desc()).limit(10).all()

    result = []
    for user in users:
        result.append({
            "username": user.username,
            "points": user.total_points
        })

    return jsonify(result)


# 📊 Analytics
@dashboard.route('/analytics/<int:user_id>', methods=['GET'])
def analytics(user_id):
    progress = UserProgress.query.filter_by(user_id=user_id).all()

    total_completed = len(progress)
    total_points = sum([p.points_earned for p in progress])

    return jsonify({
        "completed_challenges": total_completed,
        "total_points": total_points
    })