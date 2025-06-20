import psycopg2 as psy

from backend.endpoints.base_resource import BaseResource
from backend.db.orm import User

from flask import request, current_app as app

class Register(BaseResource):

    def post(self, *args, **kwargs):
        json = request.get_json()
        username = json.get("username")
        if username is None:
            return ("Missing username", 400)
        
        if not User.query.filter_by(username=username).first() is None:
            return ("Username already is use", 400)
        
        password = json.get("password")
        if password is None:
            return ("Missing password", 400)
        
        # TODO: check for secure enough password and long enough username
        hashed_password = app.bcrypt.generate_password_hash(password).decode('utf-8')
        try:
            pass #create_user(name=username, password=hashed_password)
        except psy.Error as e:
            app.logger.error(f"Error creating user with username: {username}, and pass: {password}:{e}")
            return ("Unknown error", 500)
        return (f"Registered successfully with username:{username}", 200)