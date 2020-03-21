import React from "react";

interface AnswerProps {
  userAnswer: boolean;
  correctAnswer: boolean;
}
const Answer: React.FC<AnswerProps> = ({ userAnswer, correctAnswer }) => {
  const badNotification = "Oj, to nie jest dobra odpowiedź.";
  const goodNotification = "Świetnie! Ten temat już dobrze znasz.";
  return (
    <div className="container answer ">
      <div className="row">
        <div
          className={`col-12 p-4 ${
            userAnswer === correctAnswer ? "correct" : "incorrect"
          }`}
        >
          {userAnswer === correctAnswer ? (
            <p className="text-center my-1">{goodNotification}</p>
          ) : (
            <p className="text-center my-1">{badNotification}</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Answer;
