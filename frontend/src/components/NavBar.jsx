import {Link} from "react-router-dom"

function NavBar() {
    return (
        <nav className="nav-bar">
            <div className="nav-link">
                <Link to="/"> Home </Link>
            </div>
            <div className="nav-link">
                <Link to="/login"> Login </Link>
            </div>
        </nav>
    )
}

export default NavBar