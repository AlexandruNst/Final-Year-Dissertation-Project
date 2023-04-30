import React, { useState } from "react";

// Components
import AppTitle from "components/titles/AppTitle";
import Section1 from "components/sections/Section1";
import Section2 from "components/sections/Section2";
import Section3 from "components/sections/Section3";
import Button01 from "components/buttons/Button01";
import Button12 from "components/buttons/Button12";
import Button23 from "components/buttons/Button23";
import Reset from "components/misc/Reset";

// Styles
import "./App.scss";

const App = () => {
  const [progress, setProgress] = useState(0);
  const [isUploadedS1, setIsUploadedS1] = useState(false);
  const [isReg, setIsReg] = useState(false);
  const [isUploadedS3, setIsUploadedS3] = useState(false);

  return (
    <>
      <AppTitle />
      {progress <= 0 && (
        <Button01 progress={progress} setProgress={setProgress} />
      )}
      {progress >= 1 && (
        <>
          <Section1
            progress={progress}
            setProgress={setProgress}
            isUploadedS1={isUploadedS1}
            setIsUploadedS1={setIsUploadedS1}
          />
        </>
      )}
      {progress >= 2 && (
        <Reset
          setProgress={setProgress}
          setIsUploadedS1={setIsUploadedS1}
          setIsReg={setIsReg}
          setIsUploadedS3={setIsUploadedS3}
        />
      )}
      {progress == 2 && (
        <Button12
          progress={progress}
          setProgress={setProgress}
          setIsReg={setIsReg}
        />
      )}
      {progress >= 3 && (
        <>
          <Section2 isReg={isReg} />
        </>
      )}
      {progress == 4 && (
        <>
          <Button23 progress={progress} setProgress={setProgress} />
        </>
      )}
      {progress >= 5 && (
        <>
          <Section3
            progress={progress}
            setProgress={setProgress}
            isUploadedS3={isUploadedS3}
            setIsUploadedS3={setIsUploadedS3}
          />
        </>
      )}
    </>
  );
};

export default App;
