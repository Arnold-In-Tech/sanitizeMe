import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import SignUp from './components/SignUp';
<<<<<<< HEAD
import OpenDonations from './components/OpenDonations';
import CharityDetails from './components/CharityDetails';
import Donations from './components/Donations';

const Homepage = () => <h1>Homepage</h1>;
const BrowseCharities = () => <h1>Browse Charities</h1>;
const HowItWorks = () => <h1>How It Works</h1>;
const SignIn = () => <h1>Sign In</h1>;
=======
import Login from './components/Login';
import Footer from './components/Footer';
// import Partners from './components/Partners';
import OpenDonations from './components/OpenDonations';
import CharityDetails from './components/CharityDetails';
import Donations from './components/Donations';
import Homepage from './components/Homepage';
import RegisterCharity from './components/Register_charity';
import MyCharities from './components/My_Charities'
import HowItWorks from './components/HowItWorks';
 
// const HowItWorks = () => <h1>How It Works</h1>;
const AboutUs = () => <h1>About Us</h1>;
>>>>>>> 211c2cf4cbbe949629e00297ff5142b002fa9b51

const App = () => {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Homepage />} />
<<<<<<< HEAD
        <Route path="/charities" element={<BrowseCharities />} />
        <Route path="/how-it-works" element={<HowItWorks />} />
        <Route path="/create-account" element={<SignUp />} />
        <Route path="/sign-in" element={<SignIn />} />
        <Route path="/opendonations" element={<OpenDonations />} />
        <Route path="/charities/:id" component={<CharityDetails />} />
        <Route path="/charityStories/:id" element={<CharityDetails />} />
        <Route path="/donations/:charityId" element = {<Donations />} />
=======

        <Route path="/charities" element={<OpenDonations />} />
        <Route path="/charities/:id" component={<CharityDetails />} />
        <Route path="/charityStories/:id" element={<CharityDetails />} />
        <Route path="/donations/:charityId" element = {<Donations />} />

        <Route path="/createCharities" element={<RegisterCharity />} />
        <Route path="/howItWorks" element={<HowItWorks />} />
        <Route path="/myCharities" element={<MyCharities />} />
        <Route path="/aboutUs" element={<AboutUs />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/login" element={<Login />} />
        <Route path="/login" element={<HowItWorks />} />
        {/* <Route path="/partners" element={<Partners />} /> */}

>>>>>>> 211c2cf4cbbe949629e00297ff5142b002fa9b51
      </Routes>
      <Footer />
    </Router>
    
  );
};

export default App;
