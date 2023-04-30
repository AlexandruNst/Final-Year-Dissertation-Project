import React from "react";

import "./LegendHBO.scss";

const LegendHBO = () => {
  return (
    <div id="legend">
      <div id="legend-wrapper">
        <div id="legend-text-top">&Delta;HbO (mM)</div>
        <div id="legend-color"></div>
        <div id="legend-text-bottom">
          <span>-0.3</span>
          <span>-0.2</span>
          <span>-0.1</span>
          <span>0</span>
          <span>0.1</span>
          <span>0.2</span>
          <span>0.3</span>
        </div>
      </div>
    </div>
  );
};

export default LegendHBO;
