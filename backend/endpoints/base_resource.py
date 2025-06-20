from flask_restful import Resource
from flask import request, session

class BaseResource(Resource):
    def __init__(self):
        super()
        
    def dispatch_request(self, *args, **kwargs):        
        if not request.is_json:
            return ("Not json format, this endpoint only accepts json", 400)           
        
        return super().dispatch_request(*args, **kwargs)

class LoggedInResource(BaseResource):
    def dispatch_request(self, *args, **kwargs):
        if session.get('logged in') is None or session.get('logged_in') is False:
            return ("Authentication is needed", 403)
        return super().dispatch_request(*args, **kwargs)
    
