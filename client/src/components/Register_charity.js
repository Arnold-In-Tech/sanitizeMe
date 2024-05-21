import React, { useState } from 'react';
import "../stylesheets/Register_charity.css"
import { useNavigate} from "react-router-dom";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function RegisterCharity() {
  const [flag, setFlag] = useState(1)
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    title: '',
    charity_description: '',
    organizer_name: '',
    location: '',
    period: '',
    // administrator_id, donor_id, status and total amount will be set to default "Inactive" and 0 respectively in the backend
  });
  const notify_s = () => toast("Registration successful!");
  const notify_f = () => toast("Unsuccessful - Please Login!");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Handle post request
  const handleSubmit = (e) => {
  e.preventDefault();
  fetch("/createCharities", {
      method: 'POST',
      body: JSON.stringify({
        title: formData.title,
        charity_description: formData.charity_description,
        organizer_name: formData.organizer_name,
        location: formData.location,
        period: formData.period,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
  })
      .then((res) => {
        console.log(res)
        return [res.json(), res.status, res.statusText]})
      .then((post) => {
        if (post[1] === 201) {
          setFormData({
            title: '',
            charity_description: '',
            organizer_name: '',
            location: '',
            period: '',     
          });
          setFlag(1);
          notify_s();
          setTimeout(function(){
            navigate("/charities");
         }, 5000);
        }else{
          notify_f();
          // alert("Error " + post[1] + " " + post[2] + " : registration Unsuccessful - Please Login")
          setFlag(2);  // This will display invalid login 
        }
      })
      .catch((err) => {
        console.log(err.message);
      });
  }


  return (
    <div className="register-app">
      <h2 className="register_charity">Register charity</h2>
      <form onSubmit={handleSubmit} className="form">
        <input type="text" name="title" value={formData.title} onChange={handleChange} placeholder="Enter charity title" className="form-item" />
        <textarea name="charity_description" value={formData.charity_description} onChange={handleChange} placeholder="Enter charity description" rows="4" className="form-item"></textarea>
        <input type="text" name="organizer_name" value={formData.organizer_name} onChange={handleChange} placeholder="Organization/Organizer's name" className="form-item" />
        <input type="text" name="location" value={formData.location} onChange={handleChange} placeholder="Charity location" className="form-item" />
        <input type="text" name="period" value={formData.period} onChange={handleChange} placeholder="Active period: DD/MM/YY - DD/MM/YY" className="form-item" />
        <button type="submit" className="btn">Register charity</button>
        { flag === 2 && <p style={{ color: 'red', lineHeight : 1, paddingTop: '0.5em', fontSize: "large", fontWeight: "bold", textAlign: "center" }}>Unsuccessful. Please Login First !</p>}
        <ToastContainer />
      </form>
    </div>
  );
}

export default RegisterCharity;
