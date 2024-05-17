import React from 'react';
import { Link } from 'react-router-dom'; 

const Header = () => {
  return (
      <nav className="nav">        
        <ul className="leftmenu">
          <li className="nav-item">
            <Link to="/" className="nav-link">
              sanitizeMe
            </Link>
          </li>
        </ul>

        <ul className="middlemenu">
          <li className="nav-item">
            <Link to="/browse-charities" className="nav-link">
              Charities
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/how-it-works" className="nav-link">
              How it works
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/" className="nav-link">
              My charities
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/AboutUs" className="nav-link">About Us</Link>
          </li>
          <li className="nav-item">
            <Link to="/partners" className="nav-link">Our Partners</Link>
          </li>
        </ul>

        <ul className="rightmenu"> 
          <li className="nav-item" id="signuplink">
            <Link to="/create-account" className="nav-link">
              Register
            </Link>
          </li>
          <li className="nav-item" id="loginlink">
            <Link to="/sign-in" className="nav-link">
              Sign In
            </Link>
          </li>
        </ul>
      </nav>
  );
};

export default Header;
