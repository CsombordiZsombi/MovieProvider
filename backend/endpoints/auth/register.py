# register.py
import psycopg2 as psy

from backend.endpoints.base_resource import BaseResource
from backend.db.orm import User, register_user

from flask import request, current_app as app

class Register(BaseResource):

    def post(self, *args, **kwargs):
        json = request.get_json()
        username = json.get("username")
        if username is None:
            return {"success": False, "message": "Missing username"}, 400
        
        if User.query.filter_by(username=username).first() is not None:
            return {"success": False, "message": "Username already in use"}, 400
        
        email = json.get("email")
        if email is None:
            return {"success": False, "message": "Missing email"}, 400
        
        if User.query.filter_by(email=email).first() is not None:
            return {"success": False, "message": "Email already in use"}, 400
        
        password = json.get("password")
        if password is None:
            return {"success": False, "message": "Missing password"}, 400
        
        # TODO: check for secure enough password and long enough username
        
        result = register_user(username=username, plaintext_password=password, email=email)
        return result