import React, { useState, useEffect } from 'react';

function CharityDetails({ match }) {
    const [charity, setCharity] = useState(null);
    const [charityStories, setcharityStories] = useState([]);

    useEffect(() => {
        const fetchCharityDetails = async () => {
            const charityId = match.params.id;
            try {
                // Fetch charity details
                const charityResponse = await fetch(`http://127.0.0.1:5000/charities/${charityId}`);
                const charityData = await charityResponse.json();
                setCharity(charityData);

                // Fetch beneficiary stories
                const storiesResponse = await fetch(`http://127.0.0.1:5000/charityStories/${charityId}`);
                const storiesData = await storiesResponse.json();
                setcharityStories(storiesData);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchCharityDetails()
    }, [match.params.id]);

    if (!charity) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{charity.title}</h1>
            <p>{charity.charity_description}</p>
            <h2>Benefeciary Stories</h2>
            <ul>
                {charityStories.map((story, index) => (
                    <li key={index}>
                        <strong>{story.beneficiary_name}: </strong>
                        <strong>{story.beneficiary_story}: </strong>

                    </li>
                ))}
            </ul>
        </div>
    );
}

export default CharityDetails;
