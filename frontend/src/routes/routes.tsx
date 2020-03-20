import React from "react";
import { Router } from "react-router";
import { Route, Switch, BrowserRouter, Redirect } from "react-router-dom";
import { useParams, useHistory } from "react-router";
import Cookies from "js-cookie";

// import PrivateRoute from "./PrivateRoute";
import { Header } from "../components";
import HomePageContainer from "../pages/App/App";

export const BasicParamsComponent = () => {
  const { id = "" } = useParams();

  Cookies.set("PostId", `This post id is: ${id}`, { expires: 1 });

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
      <div className="container main-view">
        <Switch>
          <Route exact={true} path="/" component={HomePageContainer} />
          <Route
            exact={true}
            path="/link1"
            component={() => {
              return <div>First link</div>;
            }}
          />
          <Route
            exact={true}
            path="/link2/:id"
            component={() => <BasicParamsComponent />}
          />
          <Redirect to={"/"} />
        </Switch>
      </div>
    </BrowserRouter>
  );
};
export default Routes;
