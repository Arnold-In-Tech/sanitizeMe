import React from 'react';
import { BrowserRouter as Router,Routes, Route,  } from 'react-router-dom';
import OpenDonations from './components/OpenDonations';
import CharityCard from './components/CharityCard';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/opendonations" Component={OpenDonations} />
        <Route path= "/charitycard" Component = {CharityCard} />
      </Routes>
        </Router>
);
}
function Home() {
  return(

    <div class="container mx-auto" >
      <h1 className= "text-5xl">Sanitize Me Donation</h1>

  </div>
)
}

export default App;
