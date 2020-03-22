import React, { useEffect, useState, ReactChild, ReactElement } from "react";
import Cookies from "js-cookie";
import { v4 as uuid } from "uuid";

const CookieHoC: React.FC<{ component: any }> = ({ component }) => {
  const [sessionID, setSessionId] = useState<string>();
  useEffect(() => {
    if (!sessionID) {
      const cookieSessionID = Cookies.get("sessionId");
      if (cookieSessionID) {
        Cookies.set("sessionId", cookieSessionID, {
          expires: 30
        }); // refresh cookie
        setSessionId(cookieSessionID);
      } else {
        const newId = uuid();
        setSessionId(newId);
        Cookies.set("sessionId", newId, { expires: 30 });
      }
    }
  }, []);
  return component;
};

export default CookieHoC;
