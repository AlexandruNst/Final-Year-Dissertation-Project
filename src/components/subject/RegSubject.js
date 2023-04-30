import React from "react";
import { useRef } from "react";
import * as THREE from "three";
import { useLoader } from "react-three-fiber";
import { PLYLoader } from "three/examples/jsm/loaders/PLYLoader";

import model_ply from "api/data/user_input/reg_ply_file.ply";

const RegSubject = ({ showBrain, showSkull, showSkin }) => {
  const group = useRef();
  const nodes = useLoader(PLYLoader, model_ply);
  const material = new THREE.PointsMaterial({
    vertexColors: nodes.attributes.color.array,
    opacity: !showBrain && !showSkull && !showSkin ? 1 : 0.08,
    transparent: true,
    size: 1.7,
    depthTest: !showBrain && !showSkull && !showSkin ? true : false,
  });

  return (
    <group ref={group}>
      <points
        geometry={nodes}
        material={material}
        rotation={[1.57, 3.14, 0]}
      ></points>
    </group>
  );
};

export default RegSubject;
