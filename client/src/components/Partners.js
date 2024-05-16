import React from 'react';
import charityNavigatorLogo from '../assets/CharityNav_Logo_Stack-1024x493.webp';
import ikeaFoundationLogo from '../assets/IKEA_Foundation_logo.webp';
import redCrossLogo from '../assets/The-Life-You-Can-Save-Logo-Square-Standard-1024x421.webp';
import consumerReportsLogo from '../assets/1200px-Consumer_Reports_logo_2016.webp';
import usaidLogo from '../assets/USAID-logo-1.webp';
import globalInnovationFundLogo from '../assets/Global-Innovation-Fund-1.webp';
import princetonUniversityLogo from '../assets/University-of-Princeton-Logo-1024x576.webp';
import googleLogo from '../assets/Google.webp';
import charityWatchLogo from '../assets/charity-watch-logo.webp';
import '../stylesheets/Partners.css';

const Partners = () => {
  return (
    <div className="partners">
      <h2>Our Partners</h2>
      <div className="logos-container">
        <div className="logos">
          <img src={charityNavigatorLogo} alt="Charity Navigator" />
          <img src={ikeaFoundationLogo} alt="IKEA FOUNDATION" />
          <img src={redCrossLogo} alt="Kenya Red Cross" />
          <img src={consumerReportsLogo} alt="Consumer Reports" />
          <img src={usaidLogo} alt="USAID" />
          <img src={globalInnovationFundLogo} alt="Global Innovation Fund" />
          <img src={princetonUniversityLogo} alt="Princeton University" />
          <img src={googleLogo} alt="Google" />
          <img src={charityWatchLogo} alt="Charity Watch" />
        </div>
      </div>
    </div>
  );
};

export default Partners;
