import React, { useState } from "react";
import Slider, { createSliderWithTooltip } from "rc-slider";
import "./HBOSlider.scss";

const SliderWithTooltip = createSliderWithTooltip(Slider);

const HBOSlider = ({ allHBO, setCurrHBO, allSizes, setVertexSize }) => {
  const [currSec, setCurrSec] = useState(0);
  const sliderChange = (second) => {
    setCurrHBO(allHBO[second - 1]);
    setVertexSize(allSizes[second - 1]);
    setCurrSec(second);
  };

  return (
    <div id="slider">
      <h2>Slide in time:</h2>
      <div id="times">
        <h3>1s</h3>
        <h2>Current: {currSec}s</h2>
        <h3>60s</h3>
      </div>

      <SliderWithTooltip
        dots
        min={1}
        max={60}
        step={1}
        onChange={sliderChange}
      />
    </div>
  );
};

export default HBOSlider;
