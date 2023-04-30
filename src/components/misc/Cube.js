import React from "react";

const Cube = () => {
  return (
    <mesh>
      <boxBufferGeometry attach="geometry" args={[100, 100, 100]} />
      <meshBasicMaterial
        attach="material"
        color="hotpink"
        opacity="1"
        transparent="true"
      />
    </mesh>
  );
};

export default Cube;
