import React, { useState, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import "./Section1Dropzone.scss";

const Section1Dropzone = ({ setIsUploaded, progress, setProgress }) => {
  const [isDropped, setIsDropped] = useState(false);

  const onDrop = useCallback((acceptedFiles) => {
    acceptedFiles.forEach((file) => {
      const reader = new FileReader();
      reader.onload = () => {
        const fileContents = reader.result;
        handleSubjectFile(fileContents);
      };
      reader.readAsText(file);
    });
  }, []);

  const handleSubjectFile = (file_contents) => {
    setIsDropped(true);
    fetch("/file", {
      method: "POST",
      body: file_contents,
    })
      .then((resp) => resp.json())
      .then((data) => {
        setIsUploaded(true);
        setProgress(2);
      });
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()} id="section1-dropzone">
      <input {...getInputProps()} />
      {!isDropped && (
        <div>
          <h2>Drag and drop subject point cloud</h2>
          <h3>...or click to upload file</h3>
          <p>Accepted files: ASCII format ply files</p>
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

export default Section1Dropzone;
