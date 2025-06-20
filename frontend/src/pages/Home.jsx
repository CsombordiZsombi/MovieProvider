import RegisterOrLogin from "../components/RegisterOrLogin"
import NavBar from "../components/NavBar";
import { useAuth } from "../context/AuthContext";

function Home() {
    
    const {user} = useAuth()

    return (
    <div>
        <NavBar></NavBar>
        {!user && <RegisterOrLogin/>}
        {user && <p> Letsgo </p>}
    </div>
    );
}

export default Home