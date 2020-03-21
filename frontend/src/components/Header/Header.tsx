import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { useTranslation } from "react-i18next";

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(true);

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
          setIsMenuOpen(prevState => {
            return !prevState;
          });
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

      <ul
        className={`navbar-nav ml-auto d-md-flex ${
          isMenuOpen
            ? "d-none"
            : "d-flex flex-column col-12 text-center font-size-larger"
        }`}
      >
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
          className="nav-link capitalized"
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
