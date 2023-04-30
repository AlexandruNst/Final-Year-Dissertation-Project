import React, { useState } from "react";
import Section3Title from "components/titles/Section3Title";
import Section3Dropzone from "components/dropzone/Section3Dropzone";
import Section3Canvas from "components/canvas/Section3Canvas";
import HBOSlider from "components/slider/HBOSlider";
import LegendHBO from "components/misc/LegendHBO";

const Section3 = ({ progress, setProgress, isUploadedS3, setIsUploadedS3 }) => {
  // const [isUploaded, setIsUploaded] = useState(false);
  const [allHBO, setAllHBO] = useState({});
  const [currHBO, setCurrHBO] = useState(null);
  const [allSizes, setAllSizes] = useState({});
  const [vertexSize, setVertexSize] = useState(null);

  return (
    <div className="section">
      <Section3Title />
      {!isUploadedS3 ? (
        <Section3Dropzone
          setIsUploaded={setIsUploadedS3}
          allHBO={allHBO}
          setAllHBO={setAllHBO}
          setCurrHBO={setCurrHBO}
          allSizes={allSizes}
          setAllSizes={setAllSizes}
          setVertexSize={setVertexSize}
        />
      ) : (
        <>
          <Section3Canvas currHBO={currHBO} vertexSize={vertexSize} />
          <LegendHBO />
          <HBOSlider
            allHBO={allHBO}
            setCurrHBO={setCurrHBO}
            allSizes={allSizes}
            setVertexSize={setVertexSize}
          />
        </>
      )}
    </div>
  );
};

export default Section3;
