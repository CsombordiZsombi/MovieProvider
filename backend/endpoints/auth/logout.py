from backend.endpoints.base_resource import BaseResource
from flask import session

class Logout(BaseResource):
    def get(self, *args, **kwargs):
        session.clear()
        session["user_id"] = None
        session["username"] = None
        session["logged_in"] = False
    
        return ({"succes":"Successfully logged out"}, 200)