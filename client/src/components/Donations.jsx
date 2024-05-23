import React, { useState } from 'react';
import PayPalPayment from "./PyplPayment";


function Donations() {
  const [phoneNumber, setPhoneNumber] = useState('');
  const [amount, setAmount] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    let headers = new Headers();
    headers.append("Authorization", "Bearer cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==");

    try {
      const response = await fetch("https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials", { headers });
      const result = await response.text();

      console.log(result);

      if (response.status === 200) {
        alert('Payment successful!');
      } else {
        alert('Payment failed. Please try again.');
      }
    } catch (error) {
      console.error(error);
      alert('An error occurred while processing the payment. Please try again.');
    }
  };

  return (
    <div className="container">
      <h1>Make a Donation</h1>
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
      <div style={{width: "55%"}}>
        <PayPalPayment/>
      </div>
    </div>
  );
}

export default Donations;