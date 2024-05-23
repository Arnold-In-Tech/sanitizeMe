import React, { useState } from 'react';
import axios from 'axios';
import lipanampesa from '../images/lipanampesa.png';
import PayPalPayment from "./PyplPayment";

function Donations() {
  const [phoneNumber, setPhoneNumber] = useState('');
  const [amount, setAmount] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/stkpush', {
        phone_number: phoneNumber,
        amount: amount,
      });
      alert('Payment successful!');
      console.log(response.data);

      setPhoneNumber('');
      setAmount('');
    } catch (error) {
      console.error(error);
      alert('Payment failed. Please try again.');
    }
  };

  return (
    <div className="sign_container">
      <h1>Make a Donation</h1>
      <img src={lipanampesa} alt="mpesa payment"  width="200" height= "100"></img>
      <form onSubmit={handleSubmit}>
        <label htmlFor="phoneNumber">Phone Number:</label>
        <input
          type="tel"
          id="phoneNumber"
          value={phoneNumber}
          onChange={(event) => setPhoneNumber(event.target.value)}
          required
        />
        <br />
        <label htmlFor="amount">Amount:</label>
        <input
          type="number"
          id="amount"
          value={amount}
          onChange={(event) => setAmount(event.target.value)}
          required
        />
        <br />
        <button type="submit">M-PESA Donate</button>
      </form>
      <div className='paypalbutton' style={{width: "66%", marginRight: "-1.2rem"}}>
        <PayPalPayment/>
      </div>
    </div>
  );
}

export default Donations;