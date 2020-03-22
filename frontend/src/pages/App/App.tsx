import React, { useState } from "react";
import { useTranslation } from "react-i18next";
import InfiniteScroll from "react-infinite-scroller";
import { Question } from "../../components";
import { getQuestions, QuestionProps } from "../../requests/AxiosRequest";
import Cookies from "js-cookie";

const App: React.FC = () => {
  const { t } = useTranslation();
  const initialQuestion = {
    pk: 0,
    title: "",
    is_true: true,
    real_answer: "",
    yes_answers: 0,
    no_answers: 0,
    up_votes: 0,
    down_votes: 0,
    keywords: [""],
    answers: null,
    votes: [],
    attachments: [],
    experts: []
  };
  const [questions, setQuestions] = useState<QuestionProps[]>([]);
  const cookieSessionID = Cookies.get("sessionId");

  const getQuestionsWrapper = async (page: any) => {
    const fetchedQuestions = await getQuestions(
      `questions${page ? `/?page=${page}&sessionID=${cookieSessionID}` : ""}`
    );
    console.log(fetchedQuestions);
    setQuestions(prevState => {
      const newState = prevState.concat(fetchedQuestions);
      return newState;
    });
  };

  return (
    <div className="App">
      <div className="container">
        <div className="row">
          <div className="col-12 d-flex flex-column text-center mb-5">
            <span className="text-white">
              {t("Weryfikujemy newsy o koronawirusie")}
            </span>
            <span className="text-muted">
              {t("Sprawdzaj swoją wiedzę i bądź na bieżąco")}
            </span>
          </div>
          <InfiniteScroll
            pageStart={1}
            loadMore={async page => await getQuestionsWrapper(page)}
            hasMore={true || false}
            initialLoad={true}
            loader={
              <div className="loader" key={0}>
                Loading ...
              </div>
            }
          >
            {questions.map(question => {
              return <Question question={question} />;
            })}
          </InfiniteScroll>
        </div>
      </div>
    </div>
  );
};

export default App;
