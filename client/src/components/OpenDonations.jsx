import React, { useState, useEffect } from 'react';
import CharityCard from './CharityCard';
import '../stylesheets/Opendonations.css'
import SearchBar from './SearchBar';

function OpenDonations() {
    const [charities, setCharities] = useState([]);

    useEffect(() => {
        // Fetch charities data from database
        fetch('http://127.0.0.1:5000/charities')
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