import React from "react";
import { useRef } from "react";
import * as THREE from "three";
import { useLoader } from "react-three-fiber";
import { PLYLoader } from "three/examples/jsm/loaders/PLYLoader";

import model_ply from "api/data/user_input/reg_ply_file.ply";

const RegSubjectHBO = () => {
  const group = useRef();
  const nodes = useLoader(PLYLoader, model_ply);

  var bottomPos = [];
  var bottomColor = [];
  var topPos = [];
  var topColor = [];
  var posArray = nodes.attributes.position.array;
  var colorArray = nodes.attributes.color.array;

  for (let i = 2; i < posArray.length; i += 3) {
    if (posArray[i] < -30) {
      bottomPos.push(posArray[i - 2]);
      bottomPos.push(posArray[i - 1]);
      bottomPos.push(posArray[i]);

      bottomColor.push(colorArray[i - 2]);
      bottomColor.push(colorArray[i - 1]);
      bottomColor.push(colorArray[i]);
    } else {
      topPos.push(posArray[i - 2]);
      topPos.push(posArray[i - 1]);
      topPos.push(posArray[i]);

      topColor.push(colorArray[i - 2]);
      topColor.push(colorArray[i - 1]);
      topColor.push(colorArray[i]);
    }
  }

  var bottomPosBuffer = new THREE.Float32BufferAttribute(bottomPos, 3);
  var bottomColorBuffer = new THREE.Float32BufferAttribute(bottomColor, 3);

  var topPosBuffer = new THREE.Float32BufferAttribute(topPos, 3);
  var topColorBuffer = new THREE.Float32BufferAttribute(topColor, 3);

  const bottomGeometry = new THREE.BufferGeometry();
  bottomGeometry.setAttribute("position", bottomPosBuffer);
  bottomGeometry.setAttribute("color", bottomColorBuffer);

  const topGeometry = new THREE.BufferGeometry();
  topGeometry.setAttribute("position", topPosBuffer);
  topGeometry.setAttribute("color", topColorBuffer);

  const topMaterial = new THREE.PointsMaterial({
    vertexColors: nodes.attributes.color.array,
    opacity: 0.1,
    transparent: true,
    size: 1.7,
    // depthTest: !showBrain && !showSkull && !showSkin ? true : false,
    depthTest: false,
  });

  const bottomMaterial = new THREE.PointsMaterial({
    vertexColors: nodes.attributes.color.array,
    opacity: 1,
    transparent: true,
    size: 1.7,
    // depthTest: !showBrain && !showSkull && !showSkin ? true : false,
    // depthTest: false,
  });

  return (
    <group ref={group}>
      <points
        geometry={topGeometry}
        material={topMaterial}
        rotation={[1.57, 3.14, 0]}
      ></points>
      <points
        geometry={bottomGeometry}
        material={bottomMaterial}
        rotation={[1.57, 3.14, 0]}
      ></points>
    </group>
  );
};

export default RegSubjectHBO;
