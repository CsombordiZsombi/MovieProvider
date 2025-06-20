import {Link} from "react-router-dom"

function RegisterOrLogin() {
    return (
        <nav className="register-or-login">
            <p className="register-or-login-title"> Register or log into your existing account </p>
            <div className="nav-link">
                <Link to="/login"> Login </Link>
            </div>
            <div className="nav-link">
                <Link to="/Register"> Register </Link>
            </div>
        </nav>
    )
}

export default RegisterOrLogin