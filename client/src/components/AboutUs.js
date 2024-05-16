import React, { useState } from 'react';

function AboutUs() {
    // State to manage the visibility of answers
    const [answersVisible, setAnswersVisible] = useState({});

    // Function to toggle the visibility of answers
    const toggleAnswerVisibility = (faqId) => {
        setAnswersVisible((prevState) => ({
            ...prevState,
            [faqId]: !prevState[faqId]
        }));
    };

    return (
        <div className="container">
            {/* Header */}
            <h1>About Us - SanitizeMe</h1>
            
            {/* Mission */}
            <section>
                <h2>Our Mission</h2>
                <p>SanitizeMe is a passion-driven initiative dedicated to empowering school girls in sub-Saharan Africa by providing access to sanitary towels and other essential supplies needed for their periods. We believe that every girl deserves the opportunity to pursue her education without the barrier of period poverty.</p>
            </section>
            
            {/* How You Can Help */}
            <section>
                <h2>How You Can Help</h2>
                <p>There are several ways you can support our cause:</p>
                <ul>
                    <li>Donate to provide sanitary towels and essential supplies</li>
                    <li>Help build schools and improve access to education</li>
                    <li>Support clean water initiatives in Africa</li>
                </ul>
                <p><a href="#donate">Donate Now</a> to make a difference in the lives of girls in sub-Saharan Africa!</p>
            </section>
            
            {/* Images */}
            <section>
                <img src="donation_graph.jpg" alt="Donation Graph" style={{ maxWidth: '100%', marginBottom: '20px' }} />
                <img src="https://www.kenyanews.go.ke/wp-content/uploads/2024/02/IMG-20240212-BUNGOMA-SCHOOLS-PHOTO-2-1200x630.jpg" alt="Children Receiving Donations" style={{ maxWidth: '100%', marginBottom: '20px' }} />
            </section>
            
            {/* Statistics */}
            <section>
                <h2>Statistics</h2>
                <p>Stay updated with our latest statistics on the impact we're making. <a href="#statistics">View Statistics</a></p>
            </section>
            
            {/* FAQ */}
            <section id="faq">
                <h2>Frequently Asked Questions</h2>
                <ul>
                    <li>
                        <strong>
                            <a href="#faq1" onClick={() => toggleAnswerVisibility('faq1')}>
                                What is SanitizeMe?
                            </a>
                        </strong>
                        {answersVisible['faq1'] && (
                            <div>
                                <p>SanitizeMe is a passion-driven initiative dedicated to empowering school girls in sub-Saharan Africa by providing access to sanitary towels and other essential supplies needed for their periods.</p>
                            </div>
                        )}
                    </li>
                    <li>
                        <strong>
                            <a href="#faq2" onClick={() => toggleAnswerVisibility('faq2')}>
                                Why is SanitizeMe important?
                            </a>
                        </strong>
                        {answersVisible['faq2'] && (
                            <div>
                                <p>SanitizeMe is important because we believe that every girl deserves the opportunity to pursue her education without the barrier of period poverty.</p>
                            </div>
                        )}
                    </li>
                     <li>
                        <strong>
                            <a href="#faq3" onClick={() => toggleAnswerVisibility('faq3')}>
                                Can I donate anonymously?
                            </a>
                        </strong>
                        {answersVisible['faq3'] && (
                            <div>
                                <p>- Yes, you can choose to donate anonymously if you prefer.</p>
                            </div>
                        )}
                    </li>
                    <li>
                        <strong>
                            <a href="#faq4" onClick={() => toggleAnswerVisibility('faq4')}>
                                What payment methods are accepted for donations?
                            </a>
                        </strong>
                        {answersVisible['faq4'] && (
                            <div>
                                <p>- We accept various payment methods including credit/debit cards, PayPal, and bank transfers. Please check our <a href="#donate">donation</a> section for more details.</p>
                            </div>
                        )}
                    </li>
                    <li>
                        <strong>
                            <a href="#faq5" onClick={() => toggleAnswerVisibility('faq5')}>
                                Can I choose which Charity to donate to?
                            </a>
                        </strong>
                        {answersVisible['faq5'] && (
                            <div>
                                <p> - Unfortunately, at this time, we are only accepting donations for SanitizeMe. However, your contribution will directly impact the lives of girls in need.</p>
                            </div>
                        )}
                    </li>
                </ul>
            </section>
            
            {/* Add a link to directly navigate to the FAQ section */}
            <p><a href="#faq">Jump to FAQ</a></p>
        </div>
    );
}

export default AboutUs;
