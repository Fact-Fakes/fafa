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

async function sendAnswers(url: string, data: any) {
  const response: any = await request({
    url,
    method: "POST",
    data
  });
  return response.data.results as QuestionProps[];
}

export { getQuestions, sendAnswers };

export default request;
