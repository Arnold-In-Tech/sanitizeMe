import React from "react";
import "../stylesheets/HowItWorks.css";
import howitworks from "../images/howitworks.jpeg";
import Programs from "./Programs";
import Faqs from "./Faqs";

function HowItWorks() {
    return (
        <div>
            <div className="works">
                <div className="right-side">
                    <img src={howitworks} className="works-image" />
                </div>
                <div className="left-side">
                    <div className="the-best">
                        <span>How SanitizeMe Works</span>
                        <div></div>
                    </div>
                    <div className="left-text">
                        <div>
                            <span className="stroke-text">we champion</span>
                            <div>
                                <span>the right's</span>
                            </div>
                            <div>
                                <span>of the people</span>
                            </div>
                            <div>
                            <span>
                                Your invaluable support is the cornerstone of our mission, enabling us to extend our reach to the most vulnerable communities worldwide.Together, we're making a tangible difference, one compassionate act at a time, fostering hope and resilience in the face of adversity.
                        </span>


                            </div>
                        </div>
                    </div>
                    {/* figures */}
                    <div className="figures">
                        <div>
                            <span>+50K</span>
                            <span> Donors</span>
                        </div>
                        <div>
                            <span>+250K</span>
                            <span> CHARITY</span>
                        </div>
                        <div>
                            <span>+300M</span>
                            <span> BENEFICIARIES</span>
                        </div>
                    </div>
                </div>
            </div>
            <Programs />
            <Faqs />
        </div>
    );
}

export default HowItWorks;
