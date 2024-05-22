import React from 'react';
import { Link } from 'react-router-dom';
import '../stylesheets/Opendonations.css';
import womenhealth from '../images/womenhealth.jpg';

function CharityCard({ title, charity_description, charityId }) {
  const limitDescription = (description, limit = 20) => {
    const words = description.split(' ');
    if (words.length > limit) {
      return words.slice(0, limit).join(' ') + '...';
    }
    return description;
  };
  return (

    <figure className="charity-card">
      <img src={womenhealth} alt="women health" className="charity-image" />
      <figcaption className="charity-caption">
        <h4>{title}</h4>
        <p>{limitDescription(charity_description, 5)}</p>
        <div className="charity-links">
          <Link to={`/charityStories/${charityId}`} className="read-more-link">Read More</Link>
          <Link to={`/donations/${charityId}`}>
            <button className="donate-button">Donate Now</button>
          </Link>
        </div>
      </figcaption>
    </figure>
  );
}

export default CharityCard;
