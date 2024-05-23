import { useState } from "react";

const Accordion = ({question, answer}) => {
  const [showInfo, setShowInfo] = useState(false);

  const toggleInfo = () => {
    setShowInfo(!showInfo);
  };

  return (
    <>
      <div className='question'>
        <h2>{question}</h2>
        <p onClick={toggleInfo}>{showInfo ? '-' : '▼'}</p>
      </div>
      <div className='answers'>
        {showInfo && <p>{answer}</p>}
      </div>
    </>
  );
};

export default Accordion;
