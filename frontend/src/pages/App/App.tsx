import React, { useEffect, useState } from "react";
import { v4 as uuid } from "uuid";
import Cookies from "js-cookie";
import { useTranslation } from "react-i18next";

import { Question } from "../../components";

const App: React.FC = () => {
  const { t } = useTranslation();
  const [sessionId, setSessionId] = useState<string>("");

  useEffect(() => {
    const cookieSessionID = Cookies.get("sessionId");
    if (cookieSessionID) {
      setSessionId(cookieSessionID);
    } else {
      const newId = uuid();
      setSessionId(newId);
      Cookies.set("sessionId", newId, { expires: 30 });
    }
  }, []);

  const initialQuestion =
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Addidisti ad extremum etiam indoctum fuisse. Duo Reges: constructio interrete. Rapior illuc, revocat autem Antiochus, nec est praeterea, quem audiamus. At multis se probavit.Sed quanta sit alias, nunc tantum possitne esse tanta. Illud non continuo, ut aeque incontentae. Tria genera cupiditatum, naturales et necessariae, naturales et non necessariae, nec naturales nec necessariae. Ita ne hoc quidem modo paria peccata sunt. Compensabatur, inquit, cum summis doloribus laetitia. Eam stabilem appellas. Progredientibus autem aetatibus sensim tardeve potius quasi nosmet ipsos cognoscimus.Dic in quovis conventu te omnia facere, ne doleas. Vitae autem degendae ratio maxime quidem illis placuit quieta. Nos vero, inquit ille; Quae quo sunt excelsiores, eo dant clariora indicia naturae.";

  return (
    <div className="App">
      <p className="text-center capitalized">
        {t("sessionId")}
        {": "} {sessionId}
      </p>
      <div className="container">
        <div className="row">
          <div className="col-6 mx-auto">
            <Question
              question={{
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
                attachments: []
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
