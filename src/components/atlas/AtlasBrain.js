import React, { useRef } from "react";
import { useLoader } from "react-three-fiber";
import * as THREE from "three";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader";

import atlas_brain_stl from "api/data/atlas_layers/gray_matter.stl";

const AtlasBrain = () => {
  const group = useRef();
  const nodes = useLoader(STLLoader, atlas_brain_stl);
  const material = new THREE.MeshStandardMaterial({
    color: 0xa02040,
    shininess: 100,
    opacity: 1,
    transparent: true,
    side: THREE.DoubleSide,
    flatShading: true,
  });

  return (
    <group ref={group}>
      <mesh
        geometry={nodes}
        material={material}
        rotation={[1.57, 3.14, 0]}
        renderOrder={3}
      ></mesh>
    </group>
  );
};

export default AtlasBrain;
