from flask import Flask, request
from flask_restful import Api
from datetime import timedelta
from flask_bcrypt import Bcrypt
from backend.db.orm import db
from sqlalchemy import inspect
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.secret_key = "secret" # TODO: replace with real secret key
    
    app.permanent_session_lifetime = timedelta(days=1)
    # Configure Bcrypt
    app.bcrypt = Bcrypt(app)

    # Update session configuration
    app.config.update(
        SESSION_COOKIE_SECURE=False,  # Disable in development
        SESSION_COOKIE_SAMESITE='Lax',  # Works better for private networks
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_DOMAIN=None  # Don't restrict domain
    )

    # Update CORS configuration
    CORS(app, 
        supports_credentials=True,
        resources={
            r"/api/*": {  # Only apply to API routes
                "origins": [
                    "http://movieprovider-frontend-1:8080",  # Docker service name
                    "http://localhost:8080"  # For local development
                ],
                "allow_headers": ["*"],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "expose_headers": ["Set-Cookie"]
            }
        }
    )

    # Configure Flask-SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = \
        f'postgresql+psycopg2://{app.config.get("DB_UNAME")}:{app.config.get("DB_PASS")}@{app.config.get("DB_HOST")}:{app.config.get("DB_PORT")}/{app.config.get("DB_NAME")}'

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable overhead

    db.init_app(app) # Initialize database connection
    with app.app_context():
        if inspect(db.engine).has_table("users") == False:
            from backend.db.init_db import init_db
            init_db()

    api = Api(app)
    from backend.endpoints.auth.login import Login
    api.add_resource(Login, '/api/login')

    from backend.endpoints.auth.register import Register
    api.add_resource(Register, '/api/register')

    from backend.endpoints.auth.login_check import LoginCheck
    api.add_resource(LoginCheck, '/api/login_check')

    from backend.endpoints.auth.logout import Logout
    api.add_resource(Logout, '/api/logout')

    from backend.endpoints.movies.list_movies import ListMovies
    api.add_resource(ListMovies, '/api/movies/list')

    from backend.utils.forward_request import forward_request
    @app.route('/<path:path>')
    def catch_all(path):
        return forward_request(request, f'{app.config["FRONTEND_URL"]}/{path}')

    @app.errorhandler(404)
    def not_found(e):
        return forward_request(request, app.config["FRONTEND_URL"])
    
    return app
    
app = create_app()
