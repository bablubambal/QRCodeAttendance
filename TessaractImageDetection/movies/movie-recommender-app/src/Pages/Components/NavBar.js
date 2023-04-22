// NavBar Component
import { Link } from "react-router-dom";
import "./styles/NavBarStyles.css";
import Logo from "./images/Logo2.png";

const NavBar = ({ isHome }) => {
    const gitRepoLink =
        "https://github.com/shohan2001/React-Flask-Movie-Recommendation-App";
    return (
        <div className="container header">
            <Link to="/home ">
                <img src={Logo} className="logo" alt="" />
            </Link>
            {/* if isHome then the button is the github button else its the home button*/}
            {isHome ? (
                <a href="/home" className="header-btn1 bouncy">
                    <i className="fas fa-home"></i> Home
                </a>
            ) : (
                <>
                
                {/* <Link
                    
                    rel="noreferrer"
                    className="header-btn1 bouncy"
                    to="/login"
                >
                    
                </Link> */}
                </>
            )}
        </div>
    );
};

export default NavBar;
