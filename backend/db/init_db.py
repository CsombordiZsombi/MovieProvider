#!/usr/bin/env python3
from backend.db.orm import db, User

def init_db():
    
    # Create all tables
    db.create_all()
    print("Database tables created successfully!")
    
    # Add initial data
    if not User.query.first():
        admin = User(username="admin", password='$2b$12$zE1XJu95RzsZIoqOFyhVReTnvO0x4hjyzIWd26v3gRNr5Ps9XVKxe', rank="admin")
        db.session.add(admin)
        db.session.commit()
        print("Added initial admin user")
