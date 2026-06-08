from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from auth.decorators import token_required
from flask import g

auth_bp = Blueprint( "auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    response, status = AuthService.register(data)

    return jsonify(response), status


@auth_bp.route("/login",methods=["POST"])
def login():

    data = request.get_json()

    response, status = AuthService.login(data)

    return jsonify(response), status


@auth_bp.route( "/me", methods=["GET"])
@token_required
def me():

    return jsonify({
        "success": True,
        "user": {
            "id": g.current_user.id,
            "name": g.current_user.name,
            "email": g.current_user.email
        }
    })