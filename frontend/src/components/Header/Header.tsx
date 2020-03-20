import React from "react";

const Header = () => {
  return (
    <div className="header fixed">
      <h2 className="brand-link">FakeBuster</h2>
      <img src="public/profile.png" alt="" />
      <ul>
        <li>
          <a className="btn btn-link" href="/link1">
            Link #1
          </a>
        </li>
        <li>
          <a className="btn btn-link" href="/link2/1231254152">
            Link #2
          </a>
        </li>
        <li>
          <a className="btn btn-link" href="#">
            Link #3
          </a>
        </li>
        <li>
          <a className="btn btn-link" href="#">
            Link #4
          </a>
        </li>
        <li>
          <a className="btn btn-link" href="#">
            Link #5
          </a>
        </li>
      </ul>
    </div>
  );
};

export default Header;
