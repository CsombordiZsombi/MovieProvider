from flask import session, request, current_app as app
from backend.endpoints.base_resource import BaseResource
from backend.db.orm import db, User


class Login(BaseResource):
    
    def post(self,*args,**kwargs):
        json = request.get_json()
        username = json.get("username")
        if username is None:
            return ('Error, no username given or email', 400)

        user = User.query.filter_by(username=username).first()

        if user is None:
            user = User.query.filter_by(email=username).first() # search if there is a user with the give email address
            if user is None:
                return ('Error, wrong username or password', 400)
        
        plaintext_password = json.get('password')
        
        if app.bcrypt.check_password_hash(user.password, plaintext_password):
            session.permanent = True
            session['logged_in'] = True
            session['username'] = user.username
            session['user_id'] = user.id
            session['email'] = user.email
            return ('Success, logged in', 200)
        
        return ('Error, wrong username or password', 400)
