import React from "react";
import Section2Title from "components/titles/Section2Title";
import Section2Canvas from "components/canvas/Section2Canvas";

const Section2 = ({ isReg }) => {
  return (
    <div className="section">
      <Section2Title />
      <Section2Canvas isReg={isReg} />
    </div>
  );
};

export default Section2;
