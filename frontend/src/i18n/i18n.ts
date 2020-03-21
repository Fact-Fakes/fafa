import i18n from "i18next";
import { initReactI18next } from "react-i18next";

import detector from "i18next-browser-languagedetector";
import backend from "i18next-xhr-backend";
import ENGLISH from "./english.json";
import POLISH from "./polish.json";

const resources = {
  en: ENGLISH,
  pl: POLISH,
};

i18n
  .use(detector)
  .use(backend)
  .use(initReactI18next || {}) // init i18next // this empty object is added for testing, don't know why but in 3 test's initReactI18next is undefined but it's not necessary in this spec test
  .init({
    resources,
    fallbackLng: "en",
    lng: "pl",
    keySeparator: false,
    debug: false,
    interpolation: {
      escapeValue: false, // not needed for react as it escapes by default
    },
  });

export default i18n;
