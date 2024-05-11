import React, { useState, useEffect } from 'react';
import CharityCard from './CharityCard';
import '../App.css';
// import SearchBar from './SearchBar';

function OpenDonations() {
    const [charities, setCharities] = useState([]);

    useEffect(() => {
        // Fetch charities data from database
        fetch('https://api-url/charities')
            .then(response => response.json())
            .then(data => setCharities(data))
            .catch(error => console.error('Error fetching charities:', error));
    }, []);

    return (
        <div class="w-50 padding-top: 1px">
            <h1 className="text-5xl">Open Donations</h1>
            <div className="charity-list">
                {charities.map(charity => (
                    <CharityCard
                        key={charity.id}
                        title={charity.title}
                        description={charity.description}
                        donateLink={charity.donateLink}
                    />
                ))}
            </div>
        </div>
    );
}

export default OpenDonations;
