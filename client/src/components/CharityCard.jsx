import React from 'react';
import { Link } from 'react-router-dom';
import '../stylesheets/Opendonations.css';
import images from '../images';

function CharityCard({ title, charity_description, charityId }) {
  const limitDescription = (description, limit = 20) => {
    const words = description.split(' ');
    if (words.length > limit) {
      return words.slice(0, limit).join(' ') + '...';
    }
    return description;
  };

  const randomImage = images[Math.floor(Math.random() * images.length)];
  console.log(randomImage)

  return (
    <figure className="charity-card">
      <Link
        to={{
          pathname: `/charityStories/${charityId}`,
          state: { randomImage },
        }}
      >
        <img src={randomImage} alt="charity" className="charity-image" />
      </Link>
      <figcaption className="charity-caption">
        <h4>{title}</h4>
        <p>{limitDescription(charity_description, 5)}</p>
        <div className="charity-links">
          <Link
            to={{
              pathname: `/charityStories/${charityId}`,
              state: { randomImage },
            }}
            className="read-more-link"
          >
            Read More
          </Link>

          <Link to={`/donations/${charityId}`}>
            <button className="donate-button">Donate Now</button>
          </Link>
        </div>
      </figcaption>
    </figure>
  );
}

export default CharityCard;