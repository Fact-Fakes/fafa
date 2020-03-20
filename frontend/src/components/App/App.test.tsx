import React from "react";
import { App } from "../../pages";
import { act } from "react-dom/test-utils";
import { MemoryRouter } from "react-router";
import { render, fireEvent, RenderResult } from "@testing-library/react";

describe("App renders correctyl", () => {
  let wrapper: RenderResult;

  beforeEach(() => {
    wrapper = render(<App />);
  });

  it("should render properly", async () => {
    expect(wrapper).toMatchSnapshot();
  });
});
