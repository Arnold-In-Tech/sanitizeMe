import React from 'react';
import { useState, useEffect } from 'react';


function SearchBar(charities, setCharities){
    const [searchTerm,setSearchTerm] = useState('');
    const [findCharities,setFindCharities] = useState([])

    function handleChange(e){
        setSearchTerm(e.target.value)
    }

    function handleSubmit(e){
        e.preventDefault();
        console.log(searchTerm);
        e.target.search.value = '';
        const charityToDisplay = charities.find((charity)=>{
            charity.title.toLowerCase().includes(searchTerm.toLowerCase())
        })
        console.log(charityToDisplay);
        setFindCharities([charityToDisplay]);
        setCharities([charityToDisplay]);
    }


    return(
        <form id="searchProduct" onSubmit={handleSubmit}>
        <input type="text" placeholder="search for product" name="search" onChange={handleChange}/>
        <button type='submit'>Search</button>
    </form>

    );
}
export default SearchBar;