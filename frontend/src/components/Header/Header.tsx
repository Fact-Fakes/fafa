import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { useTranslation } from "react-i18next";

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(true);

  const { t } = useTranslation();
  return (
    <nav className="navbar navbar-expand-md navbar-dark sticky-top bg-black2 justify-content-between">
      <a className="navbar-brand " href="/">
        <div className="d-inline-flex mb-0 flex-column">
          <h2 className="d-inline-flex mb-0">FAFA</h2>
          <span className="d-inline-flex mb-0">facts & fakes</span>
        </div>
      </a>
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
        <NavLink className="nav-link capitalized" to="/about" activeClassName="active">
          {t("about")}
        </NavLink>
        <NavLink
          className="nav-link capitalized"
          to="/questions/1"
          activeClassName="active"
        >
          {t("review")}
        </NavLink>
        <NavLink className="nav-link capitalized" to="/add" activeClassName="active">
          {t("add")}
        </NavLink>
      </ul>
    </nav>
  );
};

export default Header;
