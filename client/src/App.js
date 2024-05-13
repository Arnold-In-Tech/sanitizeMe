import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import OpenDonations from './components/OpenDonations';
import CharityDetails from './components/CharityDetails';

// const Homepage = () => <h1>Homepage</h1>;
// const BrowseCharities = () => <h1>Browse Charities</h1>;
// const HowItWorks = () => <h1>How It Works</h1>;
// const CreateAccount = () => <h1>Create Account</h1>;
// const SignIn = () => <h1>Sign In</h1>;

const App = () => {
  return (
    <Router>
      <div>
        {/* <Header /> */}
        <Routes>
          {/* <Route path="/" element={<Homepage />} /> */}
          <Route path="/opendonations" element={<OpenDonations />} />
          <Route path="/charities/:id" element={<CharityDetails />} />
          </Routes>
      </div>
    </Router>

  );
}

export default App; 
