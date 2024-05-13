
import './App.css';
import Header from './components/Header';
import Footer from './Footer';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SignUp from './components/SignUp';
import AboutUs from './AboutUs.js';

const Homepage = () => <h1>Homepage</h1>;
const BrowseCharities = () => <h1>Browse Charities</h1>;
const HowItWorks = () => <h1>How It Works</h1>;
const SignIn = () => <h1>Sign In</h1>;

const App = () => {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/charities" element={<BrowseCharities />} />
        <Route path="/how-it-works" element={<HowItWorks />} />
        <Route path="/create-account" element={<SignUp />} />
        <Route path="/sign-in" element={<SignIn />} />
        <Route path="/AboutUs" element={<AboutUs />} />
      </Routes>
      <Footer /> 
    </Router>
  );
};

export default App;
