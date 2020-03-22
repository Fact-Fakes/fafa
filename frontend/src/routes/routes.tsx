import React from "react";
import { Route, Switch, BrowserRouter } from "react-router-dom";

import { Header, ExpandedQuestion } from "../components";
import App from "../pages/App/App";
import { QuestionsPage, About, NotFound, AddQuestion } from "../pages";
import CookieHoC from "./cookieHoC";

export const Routes: React.FC = () => {
  return (
    <BrowserRouter>
      <Header />
      <div className="container main-view my-4">
        <CookieHoC
          component={
            <Switch>
              <Route exact={true} path={"/question/:id"} component={ExpandedQuestion} />
              <Route exact={false} path="/questions/:page/" component={QuestionsPage} />
              <Route exact={true} path="/about" component={About} />
              <Route exact={true} path="/add" component={AddQuestion} />
              <Route exact={true} path="/" component={App} />
              <Route component={NotFound} />
            </Switch>
          }
        />
      </div>
    </BrowserRouter>
  );
};
export default Routes;
