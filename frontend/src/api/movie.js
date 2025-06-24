// api/auth.js
import axios from 'axios';

// Set default credentials (if not already done in App.js)
axios.defaults.withCredentials = true;
const url = "http://localhost:5000"
axios.defaults.headers.common['Content-Type'] = 'application/json';

const list_movies = async () => {
    try {
        const response = await axios.get(url+"/api/movies/list");
        return response;
    } 
    catch (e) {
        return {success:false, "error":e, "response":response}
    } 
}