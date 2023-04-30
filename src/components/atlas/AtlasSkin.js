import React, { useRef } from "react";
import { useLoader } from "react-three-fiber";
import * as THREE from "three";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader";

import atlas_skin_stl from "api/data/atlas_layers/skin.stl";

const AtlasSkin = ({ showBrain, showSkull }) => {
  const group = useRef();
  const nodes = useLoader(STLLoader, atlas_skin_stl);
  const material = new THREE.MeshStandardMaterial({
    color: 0x0000ff,
    side: THREE.DoubleSide,
    depthWrite: !showBrain && !showSkull ? true : false,
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

export default AtlasSkin;
