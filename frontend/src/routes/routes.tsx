import React from "react";
import { Route, Switch, BrowserRouter, Redirect } from "react-router-dom";
import { useParams } from "react-router";
import Cookies from "js-cookie";

// import PrivateRoute from "./PrivateRoute";
import { Header } from "../components";
import App from "../pages/App/App";
import { QuestionsPage } from "../pages";

export const BasicParamsComponent = () => {
  const { id = "" } = useParams();

  Cookies.set("PostId", id, { expires: 1 });

  const cookieValue = Cookies.get("PostId");

  return (
    <div>
      The id is {id}, while the cookie value is: {cookieValue}
    </div>
  );
};

export const Routes: React.FC = () => {
  return (
    <BrowserRouter>
      <Header />
      <div className="container main-view my-4">
        <Switch>
          <Route exact={true} path="/" component={App} />
          <Route
            exact={true}
            path="/link1"
            component={() => {
              return <div>First link</div>;
            }}
          />
          <Route
            exact={false}
            path="/questions/:page"
            component={() => <QuestionsPage />}
          />
          <Route exact={true} path="/not-existing" component={() => <div>404 !</div>} />
          <Redirect to={"/"} />
        </Switch>
      </div>
    </BrowserRouter>
  );
};
export default Routes;
