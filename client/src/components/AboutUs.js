import React, { useState } from 'react';
import { Link } from 'react-router-dom'; 
import "../stylesheets/AboutUs.css";

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
            <section>
                <p>SanitizeMe is a passion-driven initiative dedicated to empowering school girls in sub-Saharan Africa by providing access to sanitary towels and other essential supplies needed for their periods. We believe that every girl deserves the opportunity to pursue her education without the barrier of period poverty.</p>
            </section>
            
            {/* Vision */}
            <section>
                <h2>Vision</h2>
                <p>At SanitizeMe, we envision a world where every girl, regardless of her circumstances, has unhindered access to education and can confidently pursue her dreams without the burden of period poverty. We aspire to create a future where menstruation is not a barrier but a natural aspect of life that does not hinder a girl's potential.</p>
            </section>

            {/* Mission */}
            <section>
                <h2>Mission</h2>
                <p>Our mission at SanitizeMe is to break the shackles of period poverty by providing school girls in sub-Saharan Africa with essential menstrual hygiene supplies and fostering an environment conducive to their education. We aim to empower these girls with the tools and resources they need to manage their periods with dignity, ensuring they can attend school regularly and participate fully in their education.</p>
            </section>

            {/* Values */}
            <section>
                <h2>Values</h2>
                <ul>
                    <li><strong>Empowerment:</strong> We believe in empowering girls with the resources and education necessary to manage their periods confidently and pursue their aspirations without hindrance.</li>
                    <li><strong>Equality:</strong> We advocate for gender equality by addressing the systemic barriers that hinder girls' access to education and opportunities.</li>
                    <li><strong>Community:</strong> We foster a sense of community by bringing together donors, volunteers, and beneficiaries to create lasting change and support sustainable development.</li>
                    <li><strong>Transparency:</strong> We operate with transparency and accountability, ensuring that every donation makes a tangible difference in the lives of the girls we serve.</li>
                    <li><strong>Impact:</strong> We are driven by a commitment to creating meaningful and sustainable impact, measuring our success by the positive change we bring to the lives of girls in sub-Saharan Africa.</li>
                </ul>
            </section>

            {/* How You Can Help */}
            <section>
                <h2>How You Can Help</h2>
                <p>There are several ways you can join us in our mission to empower girls and eradicate period poverty:</p>
                <ul>
                    <li>Donate: Your generous donations enable us to provide sanitary towels and essential supplies to school girls in need, ensuring they can manage their periods with dignity.</li>
                    <li>Support Education: Help us build schools and improve access to education for girls in sub-Saharan Africa, creating opportunities for them to thrive academically and socially.</li>
                    <li>Clean Water Initiatives: Support our efforts to provide clean water initiatives in Africa, ensuring girls have access to safe and hygienic facilities to manage their menstrual hygiene effectively.</li>
                </ul>
            </section>

            <section>
                <img src="https://www.wvi.org/sites/default/files/styles/hero_rectangle_1280x623/public/2022-03/D200-0913-105.webp?itok=x14voapu.jpg" alt="Providing clean water" style={{ maxWidth: '60%', marginBottom: '10px' }} />
                <p>Providing clean water</p>
                <img src="https://www.salaambaalaktrust.com/blog/wp-content/uploads/2022/02/Tax-Exemption-1024x683.jpg" alt="Helping Build A School" style={{ maxWidth: '60%', marginBottom: '10px' }} />
                <p>Helping Build A School</p>
                <p><Link to="/charities" className="donate-button">Donate Now</Link> to make a difference in the lives of girls in sub-Saharan Africa!</p>
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
                                <p>- We accept various payment methods including credit/debit cards, PayPal, and bank transfers. Please check our <Link to="/donate">donation</Link> section for more details.</p>
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

            {/* Contact Information */}
            <section>
                <h2>Contact Us</h2>
                <p>If you have any questions, suggestions, or would like to learn more about our initiatives, please don't hesitate to reach out to us. We value your input and are here to assist you.</p>
                <p><strong>Email:</strong> info@sanitize-me.org</p>
                <p><strong>Phone:</strong> +123-456-7890</p>
                <p><strong>Address:</strong> SanitizeMe Headquarters, 123 Main Street, Nirobi, Kenya</p>
            </section>
        </div>
    );
}

export default AboutUs;
