import React from "react";
import { useTranslation } from "react-i18next";
import InfiniteScroll from "react-infinite-scroller";

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
          {/* <InfiniteScroll
        pageStart={0}
        loadMore={getQuestions(`/?page=${page}&sessionID=${cookieSessionID}`);
    hasMore={true || false}
    loader={<div className="loader" key={0}>Loading ...</div>}
>
    {items} // <-- This is the content you want to load
</InfiniteScroll> */}
        </div>
      </div>
    </div>
  );
};

export default App;
