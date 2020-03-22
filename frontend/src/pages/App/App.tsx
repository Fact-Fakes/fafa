import React from "react";
import { useTranslation } from "react-i18next";

const App: React.FC = () => {
  const { t } = useTranslation();

  return (
    <div className="App">
      <div className="container">
        <div className="row">
          <div className="col-12 d-flex flex-column text-center">
            <span className="text-white">
              {t("Weryfikujemy newsy o koronawirusie")}
            </span>
            <span className="text-muted">
              {t("Sprawdzaj swoją wiedzę i bądź na bieżąco")}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
