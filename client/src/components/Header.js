import React from 'react';
import { useState } from 'react';
import { NavLink, Link } from 'react-router-dom'; 
import { FaSignOutAlt } from "react-icons/fa";
import { FaSignInAlt } from "react-icons/fa";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import '../App.css';

const Header = () => {
  const [loggedIn, setLoggedIn] = useState(sessionStorage.loginStatus);
  const notify = () => toast("Logged Out, Goodbye!!");

  const handleLogout = () => {
    setLoggedIn(false);
    sessionStorage.clear();
    
    fetch("/logout", {
      method: "DELETE",
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
      }).then((res) => {
        if (res.status === 204){
          notify()
        }else{
          console.log(res.status, res.statusText)
        }
      });
    }

  return (
      <nav className="nav" exact activeClassName="active">        
        <ul className="leftmenu">
          <li className="nav-item">
            <NavLink to="/" exact activeClassName="active" className="nav-link">
              sanitizeMe
            </NavLink>
          </li>
        </ul>

        <ul className="middlemenu">
          <li className="nav-item">
            <NavLink to="/charities" className="nav-link">
              Charities
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/createCharities" className="nav-link">
              Register charity
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/myCharities" className="nav-link">
              My charities
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/howItWorks" className="nav-link">
              How it works
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/aboutUs" className="nav-link">
              About Us
            </NavLink>
          </li>
        </ul>

        <ul className="rightmenu"> 
          {loggedIn ? (
            <li className="nav-item" id="loginlink" style={{backgroundColor: "#900C3F"}}>
              <Link to={"/login"}
              className="login-link"
              onClick={handleLogout}
              > <span>{sessionStorage.users} || </span>
                <span><FaSignOutAlt /> </span>
                 Logout
              </Link>
              <ToastContainer />
            </li>
          ) : (
            <li className="nav-item" id="loginlink">
              <Link to={"/login"}
              className="login-link"
              >
                <span><FaSignInAlt /> </span>
                Login/Register
              </Link>
            </li>
          )}
        </ul>
      </nav>
  );
};

export default Header;
