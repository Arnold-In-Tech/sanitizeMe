import React from "react";
import '../stylesheets/Programs.css'
import {programData} from './ProgramData.js'
import { FaArrowRight } from 'react-icons/fa';


function Programs(){
    return(
        <div className="programs" id="program">
            <div className="program-header">
                <span className="stroke-text">explore </span>
                <span>our</span>
                <span>programs</span>
            </div>
            <div className="program-category">
                {programData.map((program) =>(
                    <div className="category">
                        <span>{program.heading}</span>
                        <span>{program.details}</span>
                        <div className="join-now">
                        <span>join Now</span>  <FaArrowRight />
                        </div>
                        

                    </div>
                ))}

            </div>
            
        </div>
    )

}
export default Programs