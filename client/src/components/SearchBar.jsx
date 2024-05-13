import React, { useState } from 'react';

function SearchBar({ charities, setCharities }) {
    const [searchTerm, setSearchTerm] = useState('');


    function handleChange(e) {
        setSearchTerm(e.target.value);
    }

    function handleSubmit(e) {
        e.preventDefault();
        if (searchTerm.trim() === '') {
            setCharities(charities);
        } else {
            const filteredCharities = charities.filter((charity) =>
                charity.title.toLowerCase().includes(searchTerm.toLowerCase())
            );
            setCharities(filteredCharities);
        }
        setSearchTerm('');
    }

    return (
        <form id="searchCharity" onSubmit={handleSubmit}>
            <input type="text" placeholder="Search charity" name="search" value={searchTerm} onChange={handleChange} />
            <button type='submit'>Search</button>
        </form>
    );
}

export default SearchBar;
