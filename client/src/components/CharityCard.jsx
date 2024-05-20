import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css';
import womenhealth from '../images/womenhealth.jpg';

function CharityCard({ title, charity_description, charityId }) {
  return (
    <div classname ="grid-conatiner">
    <figure className="charity-card">
      <img src={womenhealth} alt="women health" className="charity-image" />
      <figcaption className="charity-caption">
        <h3>{title}</h3>
        <p>{charity_description}</p>
        <div className="charity-links">
          <Link to={`/charityStories/${charityId}`} className="read-more-link">Read More</Link>
          <Link to={`/donations/${charityId}`}>
            <button className="donate-button">Donate Now</button>
          </Link>
        </div>
      </figcaption>
    </figure>
    </div>
  );
}

export default CharityCard;
