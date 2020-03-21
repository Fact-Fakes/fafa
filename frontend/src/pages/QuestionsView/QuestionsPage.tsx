import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { getQuestions, QuestionProps } from "../../requests/AxiosRequest";
import { Question, Answer } from "../../components";

const QuestionsPage: React.FC = () => {
  const { page, id } = useParams();

  const initialQuestions = [
    {
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
    }
  ];

  const [questions, setQuestions] = useState<QuestionProps[]>(initialQuestions);

  useEffect(() => {
    async function getQuestionsAsyncWrapper() {
      const fetchedQuestions = await getQuestions(
        `questions${page ? `/?page=${page}` : ""}`
      );
      setQuestions(fetchedQuestions);
    }

    getQuestionsAsyncWrapper();
  }, []);

  return (
    <div className="col-12 col-md-6 mx-auto">
      {questions.map((question, index) => {
        return <Question className="my-5" key={index} question={question} />;
      })}
    </div>
  );
};

export default QuestionsPage;
