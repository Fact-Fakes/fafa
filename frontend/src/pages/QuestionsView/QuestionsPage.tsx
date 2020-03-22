import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { getQuestions, QuestionProps } from "../../requests/AxiosRequest";
import { Question, Answer } from "../../components";
import Cookies from "js-cookie";
import InfiniteScroll from "react-infinite-scroller";

const QuestionsPage: React.FC = () => {
  const { page } = useParams();

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
      answers: null, //USER answer
      votes: [],
      attachments: [],
      experts: []
    }
  ];

  const [questions, setQuestions] = useState<QuestionProps[]>(initialQuestions);
  const cookieSessionID = Cookies.get("sessionId");
  useEffect(() => {
    async function getQuestionsAsyncWrapper() {
      const fetchedQuestions = await getQuestions(
        `questions${page ? `/?page=${page}&sessionID=${cookieSessionID}` : ""}`
      );
      setQuestions(fetchedQuestions);
    }

    getQuestionsAsyncWrapper();
  }, []);

  return (
    <div className="col-12 col-md-6 mx-auto">
      {/* <InfiniteScroll
        pageStart={0}
        loadMore={getQuestions(`/?page=${page}&sessionID=${cookieSessionID}`);
    hasMore={true || false}
    loader={<div className="loader" key={0}>Loading ...</div>}
>
    {items} // <-- This is the content you want to load
</InfiniteScroll> */}

      {questions.map((question, index) => {
        return <Question className="my-5" key={index} question={question} />;
      })}
    </div>
  );
};

export default QuestionsPage;
