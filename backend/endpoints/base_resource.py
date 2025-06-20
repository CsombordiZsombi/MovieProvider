from flask_restful import Resource
from flask import request, session, current_app as app

class BaseResource(Resource):
    def __init__(self):
        super()
        
    def dispatch_request(self, *args, **kwargs):
        content_type = request.headers.get('Content-Type', '')
        app.logger.debug(content_type)
        
        if request.method != 'GET' and not content_type.lower().startswith('application/json'):
            return ("Not json format, this endpoint only accepts json. Please set contenty-type to applicaton/json", 400)           
        
        return super().dispatch_request(*args, **kwargs)

class LoggedInResource(BaseResource):
    def dispatch_request(self, *args, **kwargs):
        if session.get('logged in') is None or session.get('logged_in') is False:
            return ("Authentication is needed", 403)
        return super().dispatch_request(*args, **kwargs)
    
