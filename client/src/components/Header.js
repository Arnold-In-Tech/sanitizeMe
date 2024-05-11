import React from 'react';
import { Link } from 'react-router-dom'; 

const Header = () => {
  return (
    <header className="header">
      <nav className="nav">
        <ul className="nav-list">
          <li className="nav-item">
            <Link to="/" className="nav-link">
              Homepage
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/browse-charities" className="nav-link">
              Browse Charities
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/how-it-works" className="nav-link">
              How it Works
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/create-account" className="nav-link">
              Create Account
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/sign-in" className="nav-link">
              Sign In
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
