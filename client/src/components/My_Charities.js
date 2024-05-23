import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FaCalendar } from "react-icons/fa";
import { FaLocationDot } from "react-icons/fa6";
import arm_around from '../assets/arm_around.png';
import { FcApproval } from "react-icons/fc";
import { BiNoEntry } from "react-icons/bi";
import { BsXCircle } from "react-icons/bs";
import { GrMoney } from "react-icons/gr";
import { GiReceiveMoney } from "react-icons/gi";
import "../stylesheets/My_Charities.css"


function MyCharities() {

  const [charities, setCharities] = useState([]);

  useEffect(() => {
    const fetchCharities = async () => {
      try {
        const response = await axios.get('/myCharities');
        setCharities(response.data);
      } catch (error) {
        console.error('Error fetching charities:', error);
      }
    };
    fetchCharities();
  }, []);

  let sum = 0;
  charities.forEach(
    function sumFunction(item) {
      sum += item.total_amount;
    }
  )

  return (
    <div className="my-container"> 
      <h2 className="my-heading"><img src={arm_around} alt="arm around" className="arm-around" />My Charities</h2>
      <ul className="my-charity-grid">
        {charities.map((charity) => (
          <li key={charity.id} className="my-charity-list">
            <div className="my-charity-details">
                <h3 className={`my-charity-title ${charity.status === "Closed" ? 'my-closed' : ''}`}>{charity.title}</h3>

                <div className="my-status-amount-container">
                  {charity.status === "Active" ? (
                    <FcApproval
                      className= "my-active"
                    />
                  ) : (charity.status === "Inactive" ? (
                    <BiNoEntry 
                      className='my-inactive'
                    />
                  ) : (
                    <BsXCircle 
                      className='my-closed my-closed-icon'
                    />
                    ))  
                  }
                  <dev className="my-amount-container">
                    <p className='my-amount'>Amount</p> 
                    <p className='the-amount'><GrMoney /> KES. {charity.total_amount}</p>
                  </dev>
                </div>          

            </div>
            <div className={`my-loc-cal-container ${charity.status === "Closed" ? 'my-closed' : ''}`}>
                <p><FaLocationDot className="inline mr-2" />{charity.location}</p>
                <p><FaCalendar className="inline mr-2" />{charity.period}</p>
            </div>
        </li>
        ))}
      </ul>
      <div className='my-lower-panel'>

        <p className='my-grand-total'>
        Grand total <GiReceiveMoney className='my-gtotal-icon'/> 
          : KES. {sum}
        </p>
        <div className='my-keys'>
          <p className='my-active-name'><FcApproval className= "my-active"/> Active </p>
          <p className='my-inactive-name'><BiNoEntry className='my-inactive'/> Inactive</p>
          <p className='my-closed-name'><BsXCircle className='my-closed my-closed-icon'/> Closed</p>
        </div>
        
      </div>
    </div>
  );
}

export default MyCharities;
