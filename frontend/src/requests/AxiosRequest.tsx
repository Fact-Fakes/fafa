import axios, { AxiosRequestConfig } from "axios";
import Cookies from "js-cookie";
const COOKIE_EXPIRES = 30; // 30 days
const CSRF_ENABLED = process.env.REACT_APP_CSRF_ENABLED || false;
export const baseURL = process.env.REACT_APP_API_BASE;
if (!baseURL) {
  throw new Error("REACT_APP_API_BASE is not defined in .env file");
}
const axiosInstance = axios.create({
  baseURL,
  headers: {
    "Content-Type": "application/json"
  },
  xsrfHeaderName: "X-CSRFToken",
  xsrfCookieName: "csrftoken"
});

interface Expert {
  name: string;
  file: string;
  website: string;
}
export interface QuestionProps {
  pk: number;
  title: string;
  is_true: boolean;
  real_answer: string;
  yes_answers: number;
  no_answers: number;
  up_votes: number;
  down_votes: number;
  keywords: string[];
  answers: null | boolean;
  votes: any[];
  attachments: any[];
  experts: Expert[];
}
export interface AddAnswerProps {
  question: number;
  sessionID: string;
  users_answer: boolean;
}
export interface AddVoteProps {
  question: number;
  sessionID: string;
  updown: boolean;
}

function request<T>(config: AxiosRequestConfig) {
  return axiosInstance.request<T>(config);
}

async function getQuestions(url: string) {
  const response: any = await request({
    url,
    method: "GET"
  });
  return response.data.results as QuestionProps[];
}
async function getQuestion(url: string) {
  const response: any = await request({
    url,
    method: "GET"
  });

  console.log(response.data);
  return response.data as QuestionProps;
}

async function addAnswer(url: string, data: AddAnswerProps) {
  const response: any = await request({
    url,
    method: "POST",
    data
  });
  return response.data.results as AddAnswerProps[];
}

async function addVote(url: string, data: AddVoteProps) {
  const response: any = await request({
    url,
    method: "POST",
    data: {
      question: data.question,
      sessionID: data.sessionID,
      updown: data.updown
    }
  });
  return response.data.results as AddVoteProps[];
}

export { getQuestions, addAnswer, addVote, getQuestion };
export default request;
