from backend.endpoints.base_resource import LoggedInResource
from flask import session

class Logout(LoggedInResource):
    def post():
        session["user_id"] = None
        session["username"] = None
        session["logged_in"] = False
    
        return ({"Successfully logged out"}, 200)