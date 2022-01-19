from model.User import User
from repository.text.text_repository import TextGeneratorRepository
from utils.number_translator import NumberTranslator


class TextGenerationRepositoryImplementation(TextGeneratorRepository):

    def __init__(self):
        self.number_format = NumberTranslator()

    def createTicketDescription(self, user: User):

        #Pronome
        pronoun = self._checkPronoun(user.title)

        # Preço mensal text + preço mensal
        fullSessionPriceText, fullSessionPrice = self._getFullSessionPrice(user.session_price, user.session_quantity)

        # Preço sessão
        sessionPriceText = self._getSessionPrice(user.session_price)

        # Quantidade de sessões em texto
        sessionTimesText = self.number_format.translateNumber(user.session_quantity)

        # Datas
        sessionDaysFormatted = self._formatSessionDays(user.session_days)


        final_text = f"Recebi {pronoun} {user.title} {user.name}, a quantia de {fullSessionPriceText} (R${fullSessionPrice}) " \
                     f"referente a {sessionTimesText} sessões de psicoterapia no valor de {sessionPriceText} (R${user.session_price}) a " \
                     f"sessão, realizadas nas datas {sessionDaysFormatted} dando-lhe este recibo devida quitação."

        return final_text

    @staticmethod
    def _checkPronoun(title: str):
        if title.endswith('a'):
            return "da"
        else:
            return "de"

    def _getFullSessionPrice(self, session_price, session_quantity):
        total_value = int(session_quantity) * int(session_price)
        return self.number_format.numberToString(str(total_value)), total_value

    def _getSessionPrice(self, session_price):
        return self.number_format.numberToString(str(session_price))

    @staticmethod
    def _formatSessionDays(session_days):
        text = ""
        for idx, day in enumerate(session_days):
            text += f'{day:0>5}'
            if idx != len(session_days) - 2:
                text += ", "
            elif idx != len(session_days) - 1:
                text += " e "

        return text
