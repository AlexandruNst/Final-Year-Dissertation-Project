import React from "react";
import { useRef } from "react";
import { useLoader } from "react-three-fiber";
import { PLYLoader } from "three/examples/jsm/loaders/PLYLoader";

import model_ply from "api/data/user_input/read_ply_file.ply";

const Subject = () => {
  const group = useRef();
  const nodes = useLoader(PLYLoader, model_ply);

  return (
    <group ref={group}>
      <points geometry={nodes} rotation={[1.57, 3.14, 0]}>
        <pointsMaterial
          vertexColors={nodes.attributes.color.array}
          opacity="1"
          transparent
          normals="false"
          size={1.7}
        />
      </points>
    </group>
  );
};

export default Subject;
