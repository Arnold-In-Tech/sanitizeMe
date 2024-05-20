import React from 'react';
import { useState } from 'react';
import { NavLink, Link } from 'react-router-dom'; 
import { FaSignOutAlt } from "react-icons/fa";
import { FaSignInAlt } from "react-icons/fa";
import '../App.css';

const Header = () => {
  const [loggedIn, setLoggedIn] = useState(sessionStorage.loginStatus);

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
              onClick={() => {
                setLoggedIn(false);
                sessionStorage.clear();
                }}
              > <span>{sessionStorage.users} || </span>
                <span><FaSignOutAlt /> </span>
                 Logout
              </Link>
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
