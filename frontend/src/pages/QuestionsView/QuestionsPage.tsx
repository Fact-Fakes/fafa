import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { getQuestions, QuestionProps } from "../../requests/AxiosRequest";
import request from "../../requests/AxiosRequest";

const QuestionsPage: React.FC = () => {
  const { page, id } = useParams();
  const [results, setResults] = useState<QuestionProps[]>();

  // const idExtension = id ? `/?id=${id}` : ""; FOR FUTURE USE

  // OBECNIE NIE DZIAŁA/ CORS PROBLEM

  useEffect(() => {
    try {
      let result = getQuestions(`questions${page ? `/?page=${page}` : ""}`);
      setResults(result as any);
    } catch (e) {
      console.error(e);
    }
  }, []);

  return (
    <>
      {/* {results?.map((result, index) => {
        return <div key={index}>{result.title}</div>;
      })} */}
    </>
  );
};

export default QuestionsPage;
