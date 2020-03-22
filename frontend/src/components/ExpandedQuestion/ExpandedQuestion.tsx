import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import * as Reqests from "../../requests/AxiosRequest";
import Answer from "../Answer/Answer";
import { Question } from "../../components";
import Cookies from "js-cookie";

const ExpandedQuestion: React.FC = () => {
  const { page, id } = useParams();
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

  const [question, setQuestion] = useState<Reqests.QuestionProps>(initialQuestion);
  const [hasUserVoted, setHasUserVoted] = useState<boolean>(false);
  const cookieSessionID = Cookies.get("sessionId");

  useEffect(() => {
    async function getQuestion() {
      const fetchedQuestions = await Reqests.getQuestion(`/questions/${id}`);
      setQuestion(fetchedQuestions);
    }
    getQuestion();
    setHasUserVoted(question.answers === true || question.answers === false); // check if user of this session id already voted
  }, []);

  useEffect(() => {}, []);

  return (
    <div>
      <div className="mb-4">
        <Answer userAnswer={question.answers} correctAnswer={question.is_true} />
      </div>
      <Question expanded={hasUserVoted} question={question} />
    </div>
  );
};

export default ExpandedQuestion;
