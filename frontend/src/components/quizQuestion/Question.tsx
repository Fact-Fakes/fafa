import React from "react";
import { useTranslation } from "react-i18next";
import { QuestionProps, sendAnswers } from "../../requests/AxiosRequest";
import Cookies from "js-cookie";

const QuizQuestion: React.FC<{ question: QuestionProps; className?: string }> = ({
  className = "",
  question: {
    pk = 0,
    title = "",
    is_true = true,
    real_answer = "",
    yes_answers = 0,
    no_answers = 0,
    up_votes = 0,
    down_votes = 0,
    keywords = [""],
    answers = null,
    votes = [],
    attachments = []
  }
}) => {
  const { t } = useTranslation();
  const cookieSessionID = Cookies.get("sessionId");

  const submitAnswer = async (data: {
    question: number;
    sessionID: string;
    users_answer: boolean;
  }) => {
    const url = "/answer/add/";
    sendAnswers(url, data);
  };

  return (
    <div data-questionid={pk} className={"container border rounded " + className}>
      <div className="row">
        <div className="col-12 mt-2 mb-0">
          {keywords.map((keyword, index) => {
            return (
              <a
                key={index}
                href={"https://ourpage/tags/" + keyword}
                className="badge badge-secondary mr-1 capitalized"
              >
                {keyword}
              </a>
            );
          })}
        </div>
        <div className="col-12 mt-3 px-3">
          <a
            className="text-white quote-icon text-center"
            href={`http://ourpage/links/${pk}`}
          >
            <h3 className="mx-4">{title}</h3>
          </a>
        </div>
        <div className="container pictures pb-2">
          <div className="row">
            <div className="col-8 vh-50 d-flex mx-auto">
              <img
                className="img-fluid voting-hand-yes rounded mx-auto"
                src="https://picsum.photos/200"
                alt=""
              />
            </div>
            <div className="col-12 text-center text-muted mt-1">
              {t("Źródło z dnia")}
              {": "}
              {"30.03.2020"}
            </div>
          </div>
        </div>
      </div>
      <div className="container mb-2">
        <div className="row d-flex justify-content-around">
          <div className="col-6 d-flex justify-content-center">
            <button
              className="btn btn-dark p-2"
              style={{ borderRadius: "3em", minWidth: "7em" }}
              onClick={() => {
                submitAnswer({
                  question: pk,
                  sessionID: cookieSessionID!,
                  users_answer: true
                });
              }}
            >
              <img
                src={process.env.PUBLIC_URL + "/icons/prawda.svg"}
                className="mr-2"
                alt=""
              />
              {t("truth")}
            </button>
          </div>
          <div className="col-6 d-flex justify-content-center">
            <button
              className="btn btn-dark p-2"
              style={{ borderRadius: "3em", minWidth: "7em" }}
              onClick={() => {
                submitAnswer({
                  question: pk,
                  sessionID: cookieSessionID!,
                  users_answer: false
                });
              }}
            >
              <img
                src={process.env.PUBLIC_URL + "/icons/falsz.svg"}
                className="mr-2"
                alt=""
              />
              {t("fake")}
            </button>
          </div>
        </div>
        <div className="author-card container my-3 mx-auto">
          <div className="row mb-1 mt-4">
            <div className="col-5">
              <img
                className="img-thumbnail border-0"
                src={process.env.PUBLIC_URL + "/authors/totylkoteoria.jpg"}
              />
            </div>
            <div className="col-5 pl-0">
              <div className="d-flex flex-column">
                <span>Weryfikuje:</span>
                <h4>Łukasz Sakowski</h4>
                <a href={"/author/" + "id"} className="text-white">
                  To tylko teoria
                </a>
              </div>
            </div>
            <div className="col-2">
              <img src={process.env.PUBLIC_URL + "/icons/clock.svg"} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QuizQuestion;
