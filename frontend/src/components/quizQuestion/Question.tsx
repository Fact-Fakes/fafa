import React from "react";
import { useTranslation } from "react-i18next";

type QuizAnswer = "yes" | "no";
type Tag = { title: string; link: string };

interface QuizQuestionProps {
  questionId: number;
  questionTitle: string;
  question: string;
  answer: QuizAnswer;
  expertName: string;
  expertDetailsURL: string;
  tags: Tag[];
}

const QuizQuestion: React.FC<QuizQuestionProps> = ({
  questionId = 0,
  questionTitle = "Error: no title",
  question = "Error: no question",
  answer = "Error: no answer",
  expertName = "Error: no expert specified",
  expertDetailsURL = "Error: no expert details url",
  tags = [{ title: "No tags", link: "no link" }]
}) => {
  const { t } = useTranslation();

  return (
    <div data-questionid={questionId} className="container border rounded">
      <div className="row">
        <div className="col-12">
          {tags.map((tag, index) => {
            return (
              <a key={index} href={tag.link} className="badge badge-secondary">
                {tag.title}
              </a>
            );
          })}
        </div>
        <div className="col-12 my-3">
          <a className="text-dark" href={`http://ourpage/links/${questionId}`}>
            <h3>{questionTitle}</h3>
          </a>
        </div>
        <div className="col-6 px-1 d-flex justify-content-end voting-hand-yes">
          <img
            className="mx-auto"
            src="https://picsum.photos/200"
            alt=""
            // width={window.innerWidth > 992 ? 200 : window.innerWidth / 3}
            // height={window.innerHeight > 500 ? 200 : window.innerHeight / 3}
          />
        </div>
        <div className="col-6 px-1 d-flex justify-content-start voting-hand-no">
          <img
            className="mx-auto"
            src="https://picsum.photos/200"
            alt=""
            // width={window.innerWidth > 992 ? 200 : window.innerWidth / 3}
            // height={window.innerHeight > 500 ? 200 : window.innerHeight / 3}
          />
        </div>
        <div className="col-12 mt-2">
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
        </div>
      </div>
    </div>
  );
};

export default QuizQuestion;
