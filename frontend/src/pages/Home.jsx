import LoginPrompt from "../components/LoginPrompt.jsx";
import { useAuth } from "../context/AuthContext";
import {Link} from "react-router-dom"
import { useEffect } from "react";

function RegisterOrLogin() {
    return (
        <nav className="register-or-login">
            <p className="register-or-login-title"> Register or log into your existing account </p>
            <div className="nav-link">
                <Link to="/login"> Login </Link>
            </div>
            <div className="nav-link">
                <Link to="/register"> Register </Link>
            </div>
        </nav>
    )
}

function Home() {
    
    const {user, refreshUser} = useAuth()

    useEffect(()=>{refreshUser()}, [])

    if(!user){
        return <LoginPrompt/> 
    }

    return (
    <div>
        <p> Here is your app template </p>
    </div>
    );
}

export default Home