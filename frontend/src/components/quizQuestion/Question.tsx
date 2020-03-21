import React from "react";
import { useTranslation } from "react-i18next";
import { QuestionProps, addAnswer } from "../../requests/AxiosRequest";
import Cookies from "js-cookie";
import { Redirect } from "react-router-dom";

const QuizQuestion: React.FC<{
  question: QuestionProps;
  className?: string;
  expanded?: boolean;
}> = ({
  className = "",
  expanded = false,
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
    attachments = [],
    experts = []
  }
}) => {
  const { t } = useTranslation();
  const cookieSessionID = Cookies.get("sessionId");

  const submitAnswer = async (userChoice: boolean) => {
    const data = {
      question: pk,
      sessionID: cookieSessionID as string,
      users_answer: userChoice
    };
    const url = "/answer/add/";
    addAnswer(url, data);
  };

  const redirectUser = (id: string) => {
    return <Redirect to={`/question/${id}`} />;
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
              className="btn btn-dark p-2 text-uppercase"
              style={{ borderRadius: "3em", minWidth: "7em" }}
              onClick={() => {
                submitAnswer(true);
                redirectUser(`${pk}`);
              }}
            >
              <img
                src={process.env.PUBLIC_URL + "/icons/prawda.svg"}
                className="mr-2"
                alt=""
              />
              {t("prawda")}
            </button>
          </div>
          <div className="col-6 d-flex justify-content-center">
            <button
              className="btn btn-dark p-2 text-uppercase"
              style={{ borderRadius: "3em", minWidth: "7em" }}
              onClick={() => {
                submitAnswer(false);
                redirectUser(`${pk}`);
              }}
            >
              <img
                src={process.env.PUBLIC_URL + "/icons/falsz.svg"}
                className="mr-2"
                alt=""
              />
              {t("fałsz")}
            </button>
          </div>
        </div>
        <div className="author-card container my-3 pb-1 mx-auto">
          <div className="row mb-1 mt-4">
            <div className="col-5">
              <img
                className="img-fluid m-2 border rounded"
                src={
                  experts[0]?.file
                    ? "http://127.0.0.1:8000" + experts[0]?.file
                    : "https://picsum.photos/100"
                }
              />
            </div>
            <div className="col-5 pl-0">
              <div className="d-flex flex-column mt-4">
                <span className="font-size-small">Weryfikuje:</span>
                <h4 className="font-size-medium">{experts[0]?.name}</h4>
                <a
                  style={{ wordBreak: "break-word" }}
                  href={experts[0]?.website}
                  className="text-white"
                >
                  {experts[0]?.website}
                </a>
              </div>
            </div>
            <div className="col-2 justify-content-center align-items-start pt-3 d-flex">
              <img src={process.env.PUBLIC_URL + "/icons/clock.svg"} />
            </div>
          </div>
          <div className={`row mt-2 ${expanded ? "d-flex flex-row" : "d-none"}`}>
            <div className="col-12">
              <p className="my-2" style={{ wordBreak: "break-word" }}>
                {real_answer}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QuizQuestion;
