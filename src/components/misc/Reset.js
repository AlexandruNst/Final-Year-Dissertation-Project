import React from "react";
import "./Reset.scss";

const Reset = ({ setProgress, setIsUploadedS1, setIsReg, setIsUploadedS3 }) => {
  const restart = () => {
    setProgress(1);
    setIsUploadedS1(false);
    setIsReg(false);
    setIsUploadedS3(false);
  };

  return (
    <div>
      <a href="#section-1">
        <button id="reset-button" className="button" onClick={() => restart()}>
          Restart process
        </button>
      </a>
    </div>
  );
};

export default Reset;
