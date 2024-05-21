import React from 'react';
import Partners from './Partners';
import HumanitarianMission from './HumanitarianMission';
import '../stylesheets/Homepage.css';

const Homepage = () => (
  <div className="homepage">
    <div className="message-container">
      <h1 className="main-message">Happiness comes from your action.</h1>
      <p className="subtitle">Be part of the breakthrough and make someone's dream come true.</p>
      <div className="button-container">
        <button className="action-button">Donate Now</button>
        <button className="action-button">Watch Video</button>
      </div>
    </div>
    <div className="partners-section">
      <HumanitarianMission />
      <Partners />
    </div>
  </div>
);

export default Homepage;
