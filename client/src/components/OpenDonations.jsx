import React, { useState, useEffect } from 'react';
import CharityCard from './CharityCard';
import CharityDetails from './CharityDetails';
import '../App.css';
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
        <div class="w-50 padding-top: 1px">
            <h1 className="text-5xl md:text-6xl font-extrabold leading-tighter tracking-tighter mb-4 aos-init aos-animate" data-aos="zoom-y-out">Open<span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-teal-400"> Donations</span></h1>
            <SearchBar charities={charities} setCharities={setCharities} />
            <div className="charity-list">
                {charities.map(charity => (
                    <CharityCard
                       key={charity.id}
                        title={charity.title}
                        charity_description={charity.charity_description}
                        donateLink={charity.donateLink}
                        readMoreLink={'/charityStories/<int:id>'}
                    />

                ))}
            </div>
        </div>
    );
}

export default OpenDonations;
