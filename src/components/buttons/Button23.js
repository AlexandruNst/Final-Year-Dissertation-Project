import React from "react";
import "./Button.scss";

const Button23 = ({ progress, setProgress }) => {
  const advanceProgress = () => {
    if (progress == 4) {
      setProgress(5);
    }
  };
  return (
    <div>
      <button
        id="button23"
        className="button"
        onClick={() => advanceProgress()}
      >
        Visualise haemodynamics
      </button>
    </div>
  );
};

export default Button23;
