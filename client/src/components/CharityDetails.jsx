import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import {Link} from 'react-router-dom';
import womenhealth from '../images/womenhealth.jpg';


const CharityDetails = () => {
  const { id: charityId } = useParams();
  console.log('Charity ID:', charityId);
  const [charity, setCharity] = useState(null);
  const [charityStories, setCharityStories] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchCharityDetails = async (charityId) => {
    console.log('Fetching charity details for ID:', charityId);
    try {
      const response = await axios.get(`http://127.0.0.1:5000/charities/${charityId}`);
      console.log('Charity details:', response.data);
      setCharity(response.data);
    } catch (error) {
      console.error(`Error fetching charity details: ${error.message}`);
      setError(`Error fetching charity details: ${error.message}`);
    }
  };

  const fetchCharityStories = async (charityId) => {
    console.log('Fetching charity stories for ID:', charityId);
    try {
      const response = await fetch(`http://127.0.0.1:5000/charityStories/${charityId}`);
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
    console.log('Charity ID:', charityId);
  }, [charityId]);


  if (charity) {
    return (
      <div>
        <figure className="charity-card">
            <img src={womenhealth} alt="women health" className="charity-image" />
            <figcaption className="charity-caption"></figcaption>
            </figure>
        <h1>{charity[0].title}</h1>
        <p>{charity[0].charity_description}</p>

        <h1> Beneficiary Stories</h1>
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
}

export default CharityDetails;