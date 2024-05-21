import React from 'react';
import { Link } from 'react-router-dom';
import { FaTwitter, FaFacebookF, FaInstagram, FaLinkedinIn } from 'react-icons/fa';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-row">
        <div className="footer-col">
          <h3 className="footer-title">About</h3>
          <ul className="footer-list">
            <li className="footer-item">
              <Link to="/about/partners" className="footer-link">
                Partners
              </Link>
            </li>
            <li className="footer-item">
              <Link to="/about/faq" className="footer-link">
                FAQ
              </Link>
            </li>
            <li className="footer-item">
              <Link to="/about/helpdesk" className="footer-link">
                Helpdesk
              </Link>
            </li>
            <li className="footer-item">
              <Link to="/about/community" className="footer-link">
                Community
              </Link>
            </li>
          </ul>
        </div>
        <div className="footer-col">
          <h3 className="footer-title">Terms and Conditions</h3>
          <ul className="footer-list">
            <li className="footer-item">
              <Link to="/terms/report-violations" className="footer-link">
                Report Violations
              </Link>
            </li>
            <li className="footer-item">
              <Link to="/terms/disclaimer" className="footer-link">
                Disclaimer
              </Link>
            </li>
            <li className="footer-item">
              <Link to="/terms/policy" className="footer-link">
                Policy
              </Link>
            </li>
            <li className="footer-item">
              <Link to="/terms/missionary" className="footer-link">
                Missionary
              </Link>
            </li>
          </ul>
        </div>
        <div className="footer-col">
          <h3 className="footer-title">Stay Connected</h3>
          <ul className="footer-list social-media-list">
            <li className="footer-item">
              <a href="https://twitter.com" className="footer-link" target="_blank" rel="noopener noreferrer">
                <FaTwitter />
              </a>
            </li>
            <li className="footer-item">
              <a href="https://facebook.com" className="footer-link" target="_blank" rel="noopener noreferrer">
                <FaFacebookF />
              </a>
            </li>
            <li className="footer-item">
              <a href="https://instagram.com" className="footer-link" target="_blank" rel="noopener noreferrer">
                <FaInstagram />
              </a>
            </li>
            <li className="footer-item">
              <a href="https://linkedin.com" className="footer-link" target="_blank" rel="noopener noreferrer">
                <FaLinkedinIn />
              </a>
            </li>
          </ul>
          <ul className="footer-list">
            <li className="footer-item">
              <Link to="/newsletter" className="footer-link">
                Newsletter
              </Link>
            </li>
            <li className="footer-item">
              <Link to="/rss" className="footer-link">
                RSS Feed
              </Link>
            </li>
            <li className="footer-item">
              <Link to="/blog" className="footer-link">
                Blog
              </Link>
            </li>
          </ul>
        </div>
        <div className="footer-col">
          <h3 className="footer-title">Our Office</h3>
          <p className="footer-text">
              The Cube, Riverside Towers, 2nd Floor
              Riverside Drive<br />
              Nairobi, Kenya<br />
              contact@sanitizeme.co.ke<br />
              +254 700 000000
            </p>
          <div className="copyright">
            <p className="copyright-text">
              &copy; {new Date().getFullYear()} sanitizeMe. All Rights Reserved.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
