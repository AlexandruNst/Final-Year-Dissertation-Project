import React, { Suspense } from "react";
import { Canvas } from "react-three-fiber";
import HBOShader from "components/subject/HBOShader";
import Cube from "components/misc/Cube";
import CameraControls from "components/misc/CameraControls";
import AtlasBrainHBO from "components/atlas/AtlasBrainHBO";
import RegSubjectHBO from "components/subject/RegSubjectHBO";

const Section3Canvas = ({ currHBO, vertexSize }) => {
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
          <HBOShader currHBO={currHBO} vertexSize={vertexSize} />
          <AtlasBrainHBO />
          <RegSubjectHBO />
        </Suspense>
      </Canvas>
    </div>
  );
};

export default Section3Canvas;
