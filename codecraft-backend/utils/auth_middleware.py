from functools import wraps
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"message": "Token missing"}), 401

        # Dummy user ID (for now)
        current_user_id = 1

        return f(current_user_id, *args, **kwargs)

    return decorated