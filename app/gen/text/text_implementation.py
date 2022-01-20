from app.gen.model.Session import Session
from app.gen.model.User import User
from app.gen.text.repository import TextGeneratorRepository


class TicketTextGeneratorImpl(TextGeneratorRepository):

    def __init__(self, user: User):
        self._user: User = user
        self._session: Session = user.session

    def createTicketDescription(self):
        pronoun = self._get_pronoun()

        full_session_price_text = self._session.get_full_session_price_description()

        full_session_price = self._session.get_session_total_value()

        individual_session_price = self._session.get_session_price()

        session_quantity = self._session.get_session_quantity()

        session_days_explained = self._session.get_session_days_into_list()

        final_text = f"Recebi {pronoun} {self._user.title} {self._user.name}, a quantia de {full_session_price_text} (R${full_session_price}) " \
                     f"referente a {session_quantity} sessões de psicoterapia no valor de {individual_session_price} (R${self._session._price}) a " \
                     f"sessão, realizadas nas datas {session_days_explained} dando-lhe este recibo devida quitação."

        return final_text

    def _get_pronoun(self):
        title = self._user.title
        if title.endswith('a'):
            return "da"
        else:
            return "de"
