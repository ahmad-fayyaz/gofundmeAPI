import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FundraiserList = () => {
    const [fundraisers, setFundraisers] = useState([]);

    useEffect(() => {
        const fetchFundraisers = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/apify-data/');
                setFundraisers(response.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchFundraisers();
    }, []);

    return (
        <div>
            <h1>Fundraiser List</h1>
            <ul>
                {fundraisers.map(fundraiser => (
                    <li key={fundraiser.objectID}>
                        <h2>{fundraiser.fundname}</h2>
                        <img id="image" style={{ maxWidth: '25%', height: 'auto' }} src= {fundraiser.thumb_img_url} alt="Avatar"/> 
                        <p>Balance: {fundraiser.balance}</p>
                        <p>Progress to goal: {fundraiser.goal_progress}</p>

                        <p>Distance: {fundraiser.amount_to_goal}</p>
                        <p>Donation Count: {fundraiser.donation_count_full}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default FundraiserList;