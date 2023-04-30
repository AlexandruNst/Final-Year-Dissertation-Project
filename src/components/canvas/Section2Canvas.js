import React, { Suspense, useState } from "react";
import { Canvas } from "react-three-fiber";
import Toggle from "react-toggle";
import RegSubject from "components/subject/RegSubject";
import AtlasBrain from "components/atlas/AtlasBrain";
import AtlasSkin from "components/atlas/AtlasSkin";
import AtlasSkull from "components/atlas/AtlasSkull";
import Cube from "components/misc/Cube";
import CameraControls from "components/misc/CameraControls";

import "./Section2Canvas.scss";
import "react-toggle/style.css";

const Section2Canvas = ({ isReg }) => {
  const [showSubject, setShowSubject] = useState(true);
  const [showSkin, setShowSkin] = useState(true);
  const [showSkull, setShowSkull] = useState(true);
  const [showBrain, setShowBrain] = useState(true);

  return (
    <>
      {!isReg ? (
        <div className="canvas-div" id="reg-progress-canvas">
          <div id="canvas-pre">
            <h1>Registration in process...</h1>
            <p>This may take a while</p>
            <div id="loader"></div>
          </div>
        </div>
      ) : (
        <div className="canvas-div" id="reg-canvas">
          <Canvas style={{ background: "black" }}>
            <>
              <CameraControls />
              <directionalLight intensity={0.8} position={[-10, 10, 5]} />
              <ambientLight intensity={0.3} />
              <spotLight intensity={1} position={[150, 20, 30]} angle={1} />
              <Suspense fallback={<Cube />}>
                {showBrain && <AtlasBrain />}
                {showSkull && <AtlasSkull showBrain={showBrain} />}
                {showSkin && (
                  <AtlasSkin showBrain={showBrain} showSkull={showSkull} />
                )}
                {showSubject && (
                  <RegSubject
                    showBrain={showBrain}
                    showSkull={showSkull}
                    showSkin={showSkin}
                  />
                )}
              </Suspense>
            </>
          </Canvas>
          <div className="toggles-wrapper">
            <h2>Display options:</h2>
            <div className="ind-toggle">
              <Toggle
                id="subject"
                defaultChecked={showSubject}
                onChange={() => setShowSubject(!showSubject)}
                icons={false}
              />
              <label htmlFor="subject">Subject</label>
            </div>
            <div className="ind-toggle">
              <Toggle
                id="skin"
                defaultChecked={showSkin}
                onChange={() => setShowSkin(!showSkin)}
                icons={false}
              />
              <label htmlFor="skin">Skin</label>
            </div>
            <div className="ind-toggle">
              <Toggle
                id="skull"
                defaultChecked={showSkull}
                onChange={() => setShowSkull(!showSkull)}
                icons={false}
              />
              <label htmlFor="skull">Skull</label>
            </div>
            <div className="ind-toggle">
              <Toggle
                id="brain"
                defaultChecked={showBrain}
                onChange={() => setShowBrain(!showBrain)}
                icons={false}
              />
              <label htmlFor="brain">Brain</label>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default Section2Canvas;
