import React from "react";
import { render } from "@testing-library/react";
import App from "./App";

test("Renders app properly", () => {
  const wrapper = render(<App />);
  expect(wrapper).toMatchSnapshot();
});
