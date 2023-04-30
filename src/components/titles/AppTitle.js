import React, { useState } from "react";
import "./AppTitle.scss";

const AppTitle = () => {
  const [toggle, setToggle] = useState(false);

  return (
    <div>
      <h1 className="app-title">
        Browser-based Registration and Tomographic Reconstruction <br></br> of
        Haemodynamic Response
      </h1>
      {/* <h2 className="app-subtitle">
        This web app is created for a Final Year Project.
      </h2> */}
      <p id="toggle-text" onClick={() => setToggle(!toggle)}>
        How does it work?{" "}
        {toggle ? <span>&#x25B2;</span> : <span>&#x25BC;</span>}{" "}
      </p>
      {toggle && (
        <div className="desc">
          <p>This app has 3 consecutive sections.</p>
          <p>
            Firstly, a <strong>Subject Visualisation</strong> section, where the
            user can input a ASCII .ply file of the subject point cloud in order
            to visualise it.
          </p>
          <p>
            Secondly, a <strong>Point Cloud Registration</strong> section, where
            the subject point cloud is registed to the Atlas point cloud via the
            ICP algorithm. The registration result is then displayed.{" "}
          </p>
          <p>
            Thirdly, a <strong>Haemodynamics Reconstruction</strong> section.
            This section requires the user to upload a file containing the
            timeseries matrix of oxyhemoglobin for the cortex points (both grey
            and white matter points). This section contains a slider that allows
            the user to scroll through the keyframes of the data.
          </p>
        </div>
      )}
    </div>
  );
};

export default AppTitle;
