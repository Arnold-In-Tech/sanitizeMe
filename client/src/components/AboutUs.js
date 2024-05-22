import React, { useState } from 'react';
import { Link } from 'react-router-dom'; 
import '../stylesheets/AboutUs.css';

function AboutUs() {
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
            <h1>About Us</h1>
            
            {/* Mission */}
            <section>
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
            <p><Link to="/donate" className="donate-button">Donate Now</Link> to make a difference in the lives of girls in sub-Saharan Africa!</p>
            </section>
            
            {/* Images */}
            <section>
                <img src="https://www.wvi.org/sites/default/files/styles/hero_rectangle_1280x623/public/2022-03/D200-0913-105.webp?itok=x14voapu.jpg" alt="Children Receiving Donations" style={{ maxWidth: '60%', marginBottom: '10px' }} />
                <p>Providing clean water</p>
                <img src="https://www.salaambaalaktrust.com/blog/wp-content/uploads/2022/02/Tax-Exemption-1024x683.jpg" alt="Children Receiving Donations" style={{ maxWidth: '60%', marginBottom: '10px' }} />
                <p>Helping Build A School</p>
                <img src="https://www.google.com/search?q=helping+arumbe+village+images&sca_esv=137e48d954afa8b7&sca_upv=1&ei=6RVLZr3TAZKD9u8P_Ymk-AY&ved=0ahUKEwj968u485uGAxWSgf0HHf0ECW8Q4dUDCBA&uact=5&oq=helping+arumbe+village+images&gs_lp=Egxnd3Mtd2l6LXNlcnAiHWhlbHBpbmcgYXJ1bWJlIHZpbGxhZ2UgaW1hZ2VzMgcQIRigARgKMgcQIRigARgKSN4UUIcCWKQScAF4AZABAJgBxgKgAdYOqgEDMy02uAEDyAEA-AEBmAIHoAKdD8ICChAAGLADGNYEGEeYAwCIBgGQBgiSBwUxLjMtNqAH1Ro&sclient=gws-wiz-serp#vhid=tMe3xUfzwiGH0M&vssid=l.jpg" alt="Children Receiving Donations" style={{ maxWidth: '60%', marginBottom: '10px' }} />
            </section>
            
            <section>
                <h2>Mission</h2>
                <p>At SinitizeMe, we believe in the power of collective action to transform lives. Our mission is simple yet profound: to foster positive change by connecting passionate donors like you with impactful causes worldwide.</p>
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
        </div>
    );
}

export default AboutUs;
