import React from "react";
const AddQuestion: React.FC = () => {
  return (
    <div>
      <h3 className="text-white text-center">
        Witaj w FAFA, gdzie uleczymy łańcuszek, który do Ciebie dotarł!
      </h3>
      <p className="text-muted text-center">
        Pozwól naszym eskpertom zweryfikować plotki i podziel się tym z tymi, na których
        Ci zależy.
      </p>
      <div className="page-map">
        <p className="text-white mt-5">
          Kliknij{" "}
          <a className="text-white" href="/about">
            'about'
          </a>
          , żeby poznać zasady.
        </p>
        <p className="text-white mt-4">
          Kliknij{" "}
          <a className="text-white" href="/about">
            'review'
          </a>
          , żeby zobaczyć pomysły oczekujące na weryfikację i wskaż pytania, które są
          dla Ciebie najbardziej istotne.
        </p>
        <p className="text-white mt-4">
          Kliknij{" "}
          <a className="text-white" href="/about">
            'add'
          </a>
          , żeby przesłać łańcuszek do sprawdzenia.
        </p>
        <p className="text-white mt-4">
          Kliknij{" "}
          <a className="text-white" href="/about">
            'review'
          </a>
          , żeby sprawdzić swoją wiedzę w quizie. Tu trafi Twój łańcuszek po jego
          weryfikacji.
        </p>
      </div>{" "}
    </div>
  );
};

export default AddQuestion;
