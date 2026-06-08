from models.users import Users
from database import db
from auth.jwt_handler import create_token
from services.ai_service  import AIService

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


class AuthService:

    @staticmethod
    def register(data):

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return {
                "success": False,
                "message": "All fields are required"
            }, 400

        existing_user = Users.query.filter_by(
            email=email
        ).first()

        if existing_user:
            return {
                "success": False,
                "message": "Email already exists"
            }, 409

        hashed_password = generate_password_hash(
            password
        )

        user = Users(
            name=name,
            email=email,
            password_hash=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return {
            "success": True,
            "message": "User registered successfully"
        }, 201

    @staticmethod
    def login(data):

        email = data.get("email")
        password = data.get("password")

        user = Users.query.filter_by(
            email=email
        ).first()

        if not user:
            return {
                "success": False,
                "message": "Invalid credentials"
            }, 401

        if not check_password_hash(
            user.password_hash,
            password
        ):
            return {
                "success": False,
                "message": "Invalid credentials"
            }, 401

        token = create_token(user.id)

        return {
            "success": True,
            "access_token": token
        }, 200

