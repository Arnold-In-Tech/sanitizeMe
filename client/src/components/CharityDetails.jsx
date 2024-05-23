import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';
import '../stylesheets/Opendonations.css';
import images from '../images';

const CharityDetails = () => {
  const { id: charityId } = useParams();
  const [charity, setCharity] = useState(null);
  const [charityStories, setCharityStories] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const randomImage = images[Math.floor(Math.random() * images.length)];
  console.log(randomImage)


  const fetchCharityDetails = async (charityId) => {
    try {
<<<<<<< HEAD
      const response = await axios.get(`http://127.0.0.1:5000/charities/${charityId}`);
=======
      const response = await axios.get(`/charities/${charityId}`);
      console.log('Charity details:', response.data);
>>>>>>> 211c2cf4cbbe949629e00297ff5142b002fa9b51
      setCharity(response.data);
    } catch (error) {
      console.error(`Error fetching charity details: ${error.message}`);
      setError(`Error fetching charity details: ${error.message}`);
    }
  };

  const fetchCharityStories = async (charityId) => {
    try {
      const response = await fetch(`/charityStories/${charityId}`);
      const data = await response.json();
      setCharityStories(data);
    } catch (error) {
      setError(`Error fetching charity stories: ${error.message}`);
    }
  };

  useEffect(() => {
    if (!charityId || isNaN(parseInt(charityId, 10))) {
      setError('Invalid charity ID');
      return;
    }
    setLoading(true);
    Promise.all([fetchCharityDetails(parseInt(charityId, 10)), fetchCharityStories(parseInt(charityId, 10))]).then(() => {
      setLoading(false);
    });
  }, [charityId]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (charity) {
    return (
      <div className="charity-details">
        <figure className="charity-card">
          <img src={randomImage} alt="charity" className="charity-image" />

            <h3>{charity[0].title}</h3>
            <p>{charity[0].charity_description}</p>

        </figure>

        <h1>{charity[0].title}</h1>
        <p>{charity[0].charity_description}</p>

        <h1>Beneficiary Stories</h1>
        <ul>
          {charityStories.map((story) => (
            <li key={story.id}>
              <h2>{story.beneficiary_name}</h2>
              <p>{story.beneficiary_story}</p>
            </li>
          ))}
        </ul>
        <Link to={`/donations/${charityId}`}>
          <button className="donate-button">Donate Now</button>
        </Link>
      </div>
    );
  }

  return null;
};

export default CharityDetails;