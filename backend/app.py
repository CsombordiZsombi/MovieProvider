from flask import Flask, render_template, session
from flask_restful import Api
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from backend.db.orm import db
from sqlalchemy import inspect
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.secret_key = "secret" # TODO: replace with real secret key
    api = Api(app)
    app.permanent_session_lifetime = timedelta(seconds=10)
    # Configure Bcrypt
    app.bcrypt = Bcrypt(app)
    # CORS for frontend
    CORS(app, supports_credentials=True)

    # Configure Flask-SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = \
        f'postgresql+psycopg2://{app.config.get("DB_UNAME")}:{app.config.get("DB_PASS")}@{app.config.get("DB_HOST")}:{app.config.get("DB_PORT")}/{app.config.get("DB_NAME")}'

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable overhead

    db.init_app(app) # Initialize database connection
    with app.app_context():
        if inspect(db.engine).has_table("users") == False:
            from backend.db.init_db import init_db
            init_db()

    from backend.endpoints.login import Login
    api.add_resource(Login, '/api/login')

    from backend.endpoints.register import Register
    api.add_resource(Register, '/api/register')

    from backend.endpoints.login_check import LoginCheck
    api.add_resource(LoginCheck, '/api/login_check')

    """@app.route('/')
    def hello():
        if session.get("logged_in"):
            return f"Logged in with username:{session['username']}"
        return "Hello from Dockerized Flask!"

    @app.get('/login')
    def login_page():
        return render_template("login.html")

    @app.get('/register')
    def register_page():
        return render_template("register.html")"""
    
    return app
    
app = create_app()
