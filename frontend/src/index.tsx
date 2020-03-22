import React from "react";
import ReactDOM from "react-dom";
import Routes from "./routes/routes";
import * as serviceWorker from "./serviceWorker";
import "./styles/global.scss";

ReactDOM.render(<Routes />, document.getElementById("root"));

serviceWorker.unregister();
