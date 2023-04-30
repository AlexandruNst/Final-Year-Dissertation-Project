import React from "react";
import "./Button.scss";

const Button01 = ({ progress, setProgress }) => {
  const advanceProgress = () => {
    if (progress == 0) {
      setProgress(1);
    }
  };
  return (
    <div>
      <button
        id="button01"
        className="button"
        onClick={() => advanceProgress()}
      >
        Click to get started
      </button>
    </div>
  );
};

export default Button01;
