import React, { useState, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import "./Section1Dropzone.scss";
import * as THREE from "three";

const Section3Dropzone = ({
  setIsUploaded,
  allHBO,
  setAllHBO,
  setCurrHBO,
  allSizes,
  setAllSizes,
  setVertexSize,
}) => {
  const [isDropped, setIsDropped] = useState(false);

  const onDrop = useCallback((acceptedFiles) => {
    setIsDropped(true);

    acceptedFiles.forEach((file) => {
      const reader = new FileReader();
      reader.onload = () => {
        const fileContents = reader.result;
        handleFileHBO(fileContents);
      };
      reader.readAsText(file);
    });
  }, []);

  const handleFileHBO = (file_contents) => {
    var individuals = file_contents.split("\n");
    individuals = individuals.map((row) => row.split(" "));

    // transpose - each list element is a column in the text file
    var matrix_hbo = individuals[0].map((_, colIndex) =>
      individuals.map((row) => row[colIndex])
    );

    var currColors = {};
    var currSizes = {};
    for (let i = 0; i < matrix_hbo.length; i++) {
      const { colors, sizes } = generateVertexProps(matrix_hbo[i]);
      currColors = { ...currColors, [i]: colors };
      currSizes = { ...currSizes, [i]: sizes };
    }

    setAllHBO(currColors);
    setAllSizes(currSizes);

    setCurrHBO(allHBO["0"]);
    setVertexSize(allSizes["0"]);

    setIsUploaded(true);
  };

  const generateVertexProps = (values) => {
    values.pop();
    var vertexCols = [];
    var vertexSizes = [];
    values.map((value) => {
      vertexCols.push(0);
      vertexCols.push(parseFloat(value) > 0 ? 1 : 0);
      vertexCols.push(parseFloat(value) < 0 ? 1 : 0);

      vertexSizes.push(Math.abs(parseFloat(value)) * 150);
    });
    var vertexColsBuffer = new THREE.Float32BufferAttribute(vertexCols, 3);
    var vertexSizeBuffer = new THREE.Float32BufferAttribute(vertexSizes, 1);

    return {
      colors: vertexColsBuffer,
      sizes: vertexSizeBuffer,
    };
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()} id="section3-dropzone">
      <input {...getInputProps()} />
      {!isDropped && (
        <div>
          <h2>Drag and drop haemodynamics data</h2>
          <h3>...or click to upload file</h3>
          <p>Accepted files: txt files</p>
        </div>
      )}
      {isDropped && (
        <div>
          <p>Processing file...</p>
        </div>
      )}
    </div>
  );
};

export default Section3Dropzone;
