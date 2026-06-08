from functools import wraps
from flask import request, jsonify, g

from auth.jwt_handler import verify_token
from models.users import Users


def token_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        auth_header = request.headers.get(
            "Authorization"
        )

        if not auth_header:
            return jsonify({
                "success": False,
                "message": "Token missing"
            }), 401

        try:

            token = auth_header.split(" ")[1]

        except IndexError:

            return jsonify({
                "success": False,
                "message": "Invalid token format"
            }), 401

        user_id = verify_token(token)

        if not user_id:

            return jsonify({
                "success": False,
                "message": "Invalid or expired token"
            }), 401

        user = Users.query.get(user_id)

        if not user:

            return jsonify({
                "success": False,
                "message": "User not found"
            }), 404

        g.current_user = user

        return func(*args, **kwargs)

    return wrapper