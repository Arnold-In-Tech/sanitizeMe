import React from 'react';
import '../App.css';

function CharityCard({ title, charity_description, donateLink, readMoreLink }) {
  return (
    <div className="max-w-sm rounded overflow-hidden shadow-lg m-4">
      <img className="w-full" src="charity.jpg" alt="Charity Card " />
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">{title}</div>
        <p className="text-gray-700 text-base">{charity_description}</p>
        <div className="mt-4">
                    <a href={readMoreLink} className="text-blue-500">Read More</a>
                </div>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-2">
          <a href={donateLink}>Donate Now</a>
        </button>
      </div>
    </div>
  );
}

export default CharityCard;
