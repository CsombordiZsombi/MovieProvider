import RegisterOrLogin from "../components/RegisterOrLogin"
import NavBar from "../components/NavBar";
import { useState } from "react"

function Home() {
    
    const [loggedIn, setLoggedIn] = useState(false);

    return (
    <div>
        {loggedIn == false && <RegisterOrLogin/>}
    </div>
    );
}

export default Home