import React from "react";
import "./Button.scss";

const Button12 = ({ progress, setProgress, setIsReg }) => {
  const advanceProgress = () => {
    if (progress == 2) {
      setProgress(3);
    }
  };

  const registerSubjectICP = () => {
    fetch("/register")
      .then((resp) => resp.json())
      .then((data) => {
        setIsReg(true);
        setProgress(4);
      });
  };

  return (
    <div>
      <button
        id="button12"
        className="button"
        onClick={() => {
          advanceProgress();
          registerSubjectICP();
        }}
      >
        Register Subject to Atlas
      </button>
    </div>
  );
};

export default Button12;
