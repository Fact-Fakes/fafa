import React from "react";

const About: React.FC = () => {
  return (
    <div className="text-center">
      <h2 className="text-white">404!</h2>
      <h3 className="text-muted">
        Something went wrong and we're working on it!
        <img
          className="img-fluid"
          src={process.env.PUBLIC_URL + "/icons/wrench_icon.png"}
        ></img>
      </h3>
    </div>
  );
};

export default About;
