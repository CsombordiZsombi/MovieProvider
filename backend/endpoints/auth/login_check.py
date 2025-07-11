from backend.endpoints.base_resource import BaseResource
from flask import session

class LoginCheck(BaseResource):
    def get(self, *args, **kwargs):
        return ({
            'logged_in': session.get('logged_in', False),
            'username': session.get('username'),
            'user_id': session.get('user_id'),
            'email': session.get('email')
        }, 200)