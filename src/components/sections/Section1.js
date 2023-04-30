import React, { useState } from "react";
import Section1Title from "components/titles/Section1Title";
import Section1Dropzone from "components/dropzone/Section1Dropzone";
import Section1Canvas from "components/canvas/Section1Canvas";

const Section1 = ({ progress, setProgress, isUploadedS1, setIsUploadedS1 }) => {
  // const [isUploaded, setIsUploaded] = useState(false);

  return (
    <div className="section">
      <Section1Title />
      {!isUploadedS1 ? (
        <Section1Dropzone
          setIsUploaded={setIsUploadedS1}
          progress={progress}
          setProgress={setProgress}
        />
      ) : (
        <Section1Canvas />
      )}
    </div>
  );
};

export default Section1;
