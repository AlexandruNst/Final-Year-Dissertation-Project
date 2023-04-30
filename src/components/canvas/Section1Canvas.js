import React, { Suspense } from "react";
import { Canvas } from "react-three-fiber";
import Subject from "components/subject/Subject";
import Cube from "components/misc/Cube";
import CameraControls from "components/misc/CameraControls";

const Section1Canvas = () => {
  return (
    <div
      style={{
        height: "800px",
        marginTop: "4rem",
      }}
    >
      <Canvas style={{ background: "black" }}>
        <CameraControls />
        <directionalLight intensity={0.5} />
        <ambientLight intensity={0.5} />
        <spotLight position={[10, 15, 10]} angle={0.9} />
        <Suspense fallback={<Cube />}>
          <Subject />
        </Suspense>
      </Canvas>
    </div>
  );
};

export default Section1Canvas;
