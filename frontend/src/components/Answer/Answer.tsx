import React from "react";

interface AnswerProps {
  userAnswer: boolean;
  correctAnswer: boolean;
}
const Answer: React.FC<AnswerProps> = ({ userAnswer, correctAnswer }) => {
  const badNotification = { txt: "Oj, to nie jest dobra odpowiedź.", color: "#ea331a" };
  const goodNotification = {
    txt: "Świetnie mistrzu! Ten temat już dobrze znasz.",
    color: "#7cc245"
  };

  return (
    <div>
      {userAnswer === correctAnswer ? (
        <span className="correct">{goodNotification.txt}</span>
      ) : (
        <span className="incorrect">{badNotification.txt}</span>
      )}
    </div>
  );
};

export default Answer;
