import React from "react";

const NotFound: React.FC = () => {
  return (
    <div className="text-white text-center">
      <p>
        Zweryfikuj plotkę, wysyłając ją do naszych ekspertów przez zakładkę 'dodaj'.
      </p>
      <p>
        Sprawdź swoją wiedzę, odpowiadając na pytania wysłane przez innych
        odwiedzających oraz zweryfikowanych przez ekspertów. Znajdziesz to w zakładce
        'Quiz'.
      </p>
      <p>
        Podziel się poznanymi faktami, rozsyłając zweryfikowane, pomagające innym
        plotki. Możesz to zrobić po wykonanym quizie.
      </p>
      <p>
        Jeśli zauważysz coś, na co powinniśmy zwrócić uwagę, to odezwij się do nas
        wysyłając wiadomość na adres ...@...
      </p>
    </div>
  );
};

export default NotFound;
