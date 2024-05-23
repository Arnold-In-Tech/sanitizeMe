import React, { useState } from "react";
import Data from './FaqData';
import Accordion from './Accordion';
import '../stylesheets/Faqs.css'


function Faqs() {
    const [questions, setQuestions] = useState(Data);

    return (
        <>
            <div className='container'>
                <div className='accordion-block'>
                    {questions.map((val) => {
                        return (
                            <Accordion key={val.id} {...val} />
                        );
                    })}
                </div>
            </div>
        </>
    );
}

export default Faqs;
