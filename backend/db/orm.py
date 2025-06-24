from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(70), nullable=False)
    rank = db.Column(db.Enum('admin', 'premium', 'basic', name='user_rank'), nullable=False, default='basic')
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'User: {self.id} {self.username}, {self.rank}'

def register_user(username, email, plaintext_password=None, hashed_password=None, rank='basic'):
    # Hash the password before storing
    if not hashed_password and not plaintext_password:
        raise Exception("missing parameter plaintext_password or hashed_password")
    if not hashed_password:
        hashed_password = generate_password_hash(plaintext_password).decode('utf-8')
    
    new_user = User(
        email=email,
        username=username,
        password=hashed_password,
        rank=rank
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return ({"success": True, "user_id": new_user.id}, 200)
    except Exception as e:
        db.session.rollback()
        return ({"success": False, "error": str(e)}, 500)
    

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    path = db.Column(db.String(200), nullable=False)
    icon_path = db.Column(db.String(200))
    description = db.Column(db.String(1200))
    age_restriction = db.Column(db.Integer)
    release_year = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    
    def __repr__(self):
        return f'Movie: {self.title} ({self.release_year})'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'path': self.path,
            'icon_path': self.icon_path,
            'description': self.description,
            'age_restriction': self.age_restriction,
            'release_year': self.release_year,
            'duration': self.duration,
        }
    
def create_movie(title, path, description=None, icon_path=None, age_restriction=None, release_year=None, duration=None):
    new_movie = Movie(title=title, path=path, icon_path=icon_path, description=description, age_restriction=age_restriction, release_year=release_year, duration=duration)

    try:
        db.session.add(new_movie)
        db.session.commit()
        return ({"success": True, "movie_id": new_movie.id}, 200)
    except Exception as e:
        db.session.rollback()
        return ({"success": False, "error": str(e)}, 500)
