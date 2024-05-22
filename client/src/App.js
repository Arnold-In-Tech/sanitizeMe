import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import SignUp from './components/SignUp';
import Login from './components/Login';
import Footer from './components/Footer';
// import Partners from './components/Partners';
import OpenDonations from './components/OpenDonations';
import CharityDetails from './components/CharityDetails';
import Donations from './components/Donations';
import AboutUs from './components/AboutUs';

const Homepage = () => <h1>Homepage</h1>;
const CreateCharities = () => <h1>Create charity</h1>;
const HowItWorks = () => <h1>How It Works</h1>;
const MyCharities = () => <h1>My charities</h1>;

const App = () => {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Homepage />} />

        <Route path="/charities" element={<OpenDonations />} />
        <Route path="/charities/:id" component={<CharityDetails />} />
        <Route path="/charityStories/:id" element={<CharityDetails />} />
        <Route path="/donations/:charityId" element = {<Donations />} />

        <Route path="/createCharities" element={<CreateCharities />} />
        <Route path="/howItWorks" element={<HowItWorks />} />
        <Route path="/myCharities" element={<MyCharities />} />
        <Route path="/AboutUs" element={<AboutUs />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/login" element={<Login />} />
        {/* <Route path="/partners" element={<Partners />} /> */}

      </Routes>
      <Footer />
    </Router>
    
  );
};

export default App;
