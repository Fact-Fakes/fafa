import React, { useEffect, useState } from "react";
import { v4 as uuid } from "uuid";
import Cookies from "js-cookie";
import { useTranslation } from "react-i18next";

import { Question } from "../../components";

const App: React.FC = () => {
  const { t } = useTranslation();
  const [sessionId, setSessionId] = useState<string>("");

  useEffect(() => {
    const cookieSessionID = Cookies.get("sessionId");
    if (cookieSessionID) {
      Cookies.set("sessionId", cookieSessionID, { expires: 30 }); // refresh cookie
      setSessionId(cookieSessionID);
    } else {
      const newId = uuid();
      setSessionId(newId);
      Cookies.set("sessionId", newId, { expires: 30 });
    }
  }, []);

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
