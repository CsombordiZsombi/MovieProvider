from backend.endpoints.base_resource import LoggedInResource
from flask import session

class LoginCheck(LoggedInResource):
    def get(self, *args, **kwargs):
        return {
            'logged_in': session.get('logged_in', False),
            'username': session.get('username'),
            'user_id': session.get('user_id')
        }, 200