import React, { useRef } from "react";
import { useLoader } from "react-three-fiber";
import * as THREE from "three";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader";

import atlas_skull_stl from "api/data/atlas_layers/skull.stl";

const AtlasSkull = ({ showBrain }) => {
  const group = useRef();
  const nodes = useLoader(STLLoader, atlas_skull_stl);
  const material = new THREE.MeshStandardMaterial({
    color: 0xe3dac9,
    opacity: 1,
    transparent: true,
    side: THREE.DoubleSide,
    depthWrite: showBrain ? false : true,
  });

  return (
    <group ref={group}>
      <mesh
        geometry={nodes}
        material={material}
        rotation={[1.57, 3.14, 0]}
      ></mesh>
    </group>
  );
};

export default AtlasSkull;
