from backend.endpoints.base_resource import LoggedInResource, BaseResource
from backend.db.orm import Movie

class ListMovies(BaseResource):
    def get(self, *args, **kwargs):
        movies = Movie.query.all()
        return {"movies":[movie.to_dict() for movie in movies]}, 200