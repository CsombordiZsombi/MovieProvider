#!/usr/bin/env python3
from backend.db.orm import db, register_user, create_movie

def init_db():
    
    # Create all tables
    db.create_all()
    print("Database tables created successfully!")
   
    register_user(username="admin", email="admin@domain.com",hashed_password='$2b$12$zE1XJu95RzsZIoqOFyhVReTnvO0x4hjyzIWd26v3gRNr5Ps9XVKxe', rank="admin")

    create_movie(title="test", path="./backed/test/", icon_path="https://media.themoviedb.org/t/p/w220_and_h330_face/giAiJSwOJcfA8Y4PCNMGAhfTSyA.jpg")
    create_movie(title="test2", path="./backed/test/", icon_path="https://media.themoviedb.org/t/p/w220_and_h330_face/giAiJSwOJcfA8Y4PCNMGAhfTSyA.jpg")
    
