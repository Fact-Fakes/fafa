import React from "react";
import { useTranslation } from "react-i18next";
import { QuestionProps } from "../../requests/AxiosRequest";

// oldinitial = questionId = 0
// questionTitle = "Error: no title"
// question = "Error: no question"
// answer = "Error: no answer"
// expertName = "Error: no expert specified"
// expertDetailsURL = "Error: no expert details url"
// tags = [{ title: "No tags", link: "no link" }]

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
        <div className="col-12 my-1">
          <a className="text-dark" href={`http://ourpage/links/${pk}`}>
            <h3>{title}</h3>
          </a>
        </div>
        <div className="container pictures pb-4">
          <div className="row">
            <div className="col-8 vh-50 d-flex justify-content-end">
              <img
                className="ml-auto img-fluid voting-hand-yes rounded"
                src="https://picsum.photos/200"
                alt=""
              />
            </div>
            {/* <div className="col-6 d-flex justify-content-start">
              <img
                className="mr-auto img-thumbnail voting-hand-no rounded"
                src="https://picsum.photos/200"
                alt=""
              />
            </div> */}
            <div className="col-12 text-center text-muted">
              {t("Źródło z dnia")}
              {": "}
              {"30.03.2020"}
            </div>
          </div>
        </div>
        {/* <div className="col-12 mt-2">
          <p className="capitalized">
            {t("ourExpert")}
            {", "}
            <a
              href={
                expertDetailsURL.includes("https://")
                  ? expertDetailsURL
                  : "https://" + expertDetailsURL
              }
            >
              {expertName}
            </a>{" "}
            {t("answers")}
            {": "}
          </p>
        </div> */}{" "}
        {/*For when we have experts in our excel*/}
      </div>
    </div>
  );
};

export default QuizQuestion;
