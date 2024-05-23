import React, { useState, useEffect } from 'react';
import CharityCard from './CharityCard';
<<<<<<< HEAD
import '../stylesheets/Opendonations.css'
=======
import '../App.css';
>>>>>>> 211c2cf4cbbe949629e00297ff5142b002fa9b51
import SearchBar from './SearchBar';

function OpenDonations() {
    const [charities, setCharities] = useState([]);

    useEffect(() => {
        // Fetch charities data from database
        fetch('/charities')
            .then(response => response.json())
            .then(data => setCharities(data))
            .catch(error => console.error('Error fetching charities:', error));
    }, []);

        return (
            <div>
                <div className="container">
                    <h1>Open Donations</h1>
                    <SearchBar charities={charities} setCharities={setCharities} />
                </div>
                <div className="container-charity">
                    <div className="charity-grid">
                        {charities.map(charity => (
                            <CharityCard
                                key={charity.id}
                                title={charity.title}
                                charity_description={charity.charity_description}
                                donateLink={charity.donateLink}
                                charityId={charity.id}
                            />
                        ))}
                    </div>
                </div>
            </div>
        );
    }

export default OpenDonations;