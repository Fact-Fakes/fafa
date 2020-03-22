import React, { useEffect, useState } from "react";
import { v4 as uuid } from "uuid";
import { Route, Switch, BrowserRouter, Redirect } from "react-router-dom";
import { useParams } from "react-router";
import Cookies from "js-cookie";

import { Header, Question, ExpandedQuestion } from "../components";
import App from "../pages/App/App";
import { QuestionsPage } from "../pages";

export const Routes: React.FC = () => {
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
    <BrowserRouter>
      <Header />
      <div className="container main-view my-4">
        <Switch>
          <Route exact={true} path="/" component={App} />
          <Route
            exact={true}
            path="/about"
            component={() => {
              return <div>About</div>;
            }}
          />
          <Route
            exact={true}
            path={"/question/:id"}
            component={() => <ExpandedQuestion />}
          />
          <Route
            exact={false}
            path="/questions/:page"
            component={() => <QuestionsPage />}
          />
          <Route
            component={() => {
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
            }}
          />
        </Switch>
      </div>
    </BrowserRouter>
  );
};
export default Routes;
