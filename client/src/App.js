import './App.css';
import Header from './components/Header';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SignUp from './components/SignUp';
import Footer from './components/Footer';
import Partners from './components/Partners';
import OpenDonations from './components/OpenDonations';
import CharityDetails from './components/CharityDetails';
import Donations from './components/Donations';
import Homepage from './components/Homepage';





const HowItWorks = () => <h1>How It Works</h1>;
const SignIn = () => <h1>Sign In</h1>;

const App = () => {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/how-it-works" element={<HowItWorks />} />
        <Route path="/create-account" element={<SignUp />} />
        <Route path="/sign-in" element={<SignIn />} />
        <Route path="/partners" element={<Partners />} />

        <Route path="/charities" element={<OpenDonations />} />
        <Route path="/charities/:id" component={<CharityDetails />} />
        <Route path="/charityStories/:id" element={<CharityDetails />} />
        <Route path="/donations/:charityId" element = {<Donations />} />

      </Routes>
      <Footer />
    </Router>
    
  );
};

export default App;
