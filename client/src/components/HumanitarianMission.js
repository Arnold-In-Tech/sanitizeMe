import React from 'react';
import '../stylesheets/HumanitarianMission.css';

const HumanitarianMission = () => {
  return (
    <div className="humanitarian-mission">
      <h2>Humanitarian Mission</h2>
      <div className="statistics">
        <div className="stat-item">
          <h3>130,652</h3>
          <p>Donors have given directly</p>
        </div>
        <div className="stat-item">
          <h3>92%</h3>
          <p>Donations delivered to those in need, after costs</p>
        </div>
        <div className="stat-item">
          <h3>20M+</h3>
          <p>Kenya Shillings delivered to people across 10 counties</p>
        </div>
        <div className="stat-item">
          <h3>6</h3>
          <p>Academic studies on our programs</p>
        </div>
      </div>
    </div>
  );
};

export default HumanitarianMission;
