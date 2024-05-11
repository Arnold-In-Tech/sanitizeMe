import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

const Homepage = () => <h1>Homepage</h1>;
const BrowseCharities = () => <h1>Browse Charities</h1>;
const HowItWorks = () => <h1>How It Works</h1>;
const CreateAccount = () => <h1>Create Account</h1>;
const SignIn = () => <h1>Sign In</h1>;

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
