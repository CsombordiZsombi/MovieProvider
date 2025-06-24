
function MovieCard({movie}) {

    return (
    <div className="movie-card" onClick={() => {alert(movie.title + "clicked")}}>
        <div className="movie-poster">
            <img src={movie.icon_url} alt={movie.title}/>
        </div>
        <div className="movie-info">
            <h3>{movie.title}</h3>
            <p>{movie.release_year}</p>
        </div>
    </div>
    )
    
}

export default MovieCard