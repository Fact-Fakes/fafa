import React from "react";
import { NavLink } from "react-router-dom";
import { useTranslation } from "react-i18next";

const Header = () => {
  const { t } = useTranslation();
  return (
    <nav className="navbar navbar-expand-md navbar-light bg-light sticky-top navbar justify-content-between">
      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
        onClick={() => {
          console.log("Menu expanded!");
        }}
      >
        <span className="navbar-toggler-icon"></span>
      </button>
      <a className="navbar-brand" href="#">
        <img
          src="./public/profile.png"
          width="30"
          height="30"
          className="d-inline-block align-top"
          alt=""
        />
        <h2 className="d-inline-flex mb-0">FakeBuster</h2>
      </a>

      <ul className="navbar-nav ml-auto d-md-flex d-none">
        <NavLink
          exact={true}
          className="nav-link  capitalized"
          to="/"
          activeClassName="active"
        >
          {t("browse")} <span className="sr-only">{t("active")}</span>
        </NavLink>
        <NavLink className="nav-link capitalized" to="/link1" activeClassName="active">
          {t("rules")}
        </NavLink>
        <NavLink
          className="nav-link capitalized"
          to="/questions/1"
          activeClassName="active"
        >
          {t("queue")}
        </NavLink>
        <NavLink
          className="btn btn-link capitalized"
          to="/not-existing"
          activeClassName="active"
        >
          {t("add")}
        </NavLink>
      </ul>
    </nav>
  );
};

export default Header;
