import React from "react";
import * as THREE from "three";
import { useLoader } from "react-three-fiber";
import { PLYLoader } from "three/examples/jsm/loaders/PLYLoader";

import cortex_ply from "api/data/atlas_layers/cortex.ply";
import texture_path_spark from "api/data/atlas_layers/spark1.png";

const HBOShader = ({ currHBO, vertexSize }) => {
  function vertexShader() {
    return `
      attribute float size;
			attribute vec4 ca;

			varying vec4 vColor;

			void main() {

				vColor = ca;

				vec4 mvPosition = modelViewMatrix * vec4( position, 1.0 );

				gl_PointSize = size * ( 150.0 / -mvPosition.z );

				gl_Position = projectionMatrix * mvPosition;

			}
  `;
  }

  function fragmentShader() {
    return `
      uniform vec3 color;
			uniform sampler2D pointTexture;

			varying vec4 vColor;

			void main() {

				vec4 outColor = texture2D( pointTexture, gl_PointCoord );

				if ( outColor.a < 0.5 ) discard;

				gl_FragColor = outColor * vec4( color * vColor.xyz, 1.0 );

				float depth = gl_FragCoord.z / gl_FragCoord.w;
				const vec3 fogColor = vec3( 0.0 );

				float fogFactor = smoothstep( 200.0, 600.0, depth );
				gl_FragColor = mix( gl_FragColor, vec4( fogColor, gl_FragColor.w ), fogFactor );

			}
    `;
  }

  const nodes = useLoader(PLYLoader, cortex_ply);

  if (currHBO != null) {
    nodes.setAttribute("ca", currHBO);
  }

  if (vertexSize != null) {
    nodes.setAttribute("size", vertexSize);
  }

  const texture = new THREE.TextureLoader().load(texture_path_spark);
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;

  const material = new THREE.ShaderMaterial({
    uniforms: {
      amplitude: { value: 30.0 },
      color: { value: new THREE.Color(0xffffff) },
      pointTexture: { value: texture },
      size: { value: 3 },
    },
    fragmentShader: fragmentShader(),
    vertexShader: vertexShader(),
    depthWrite: false,
    blending: THREE.AdditiveBlending,
    depthTest: false,
    transparent: true,
  });

  return (
    <points
      geometry={nodes}
      material={material}
      rotation={[1.57, 3.14, 0]}
      renderOrder={3}
    ></points>
  );
};

export default HBOShader;
