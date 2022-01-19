from utils.number_translator import NumberTranslator


class Session:

    def __init__(self, price, days):
        self.session_price = price
        self._session_days = days
        self._session_quantity = len(days)

    def get_full_session_price_description(self):
        total_value = self.get_session_total_value()
        return NumberTranslator().numberToString(str(total_value))

    def get_session_total_value(self):
        total_value = int(self._session_quantity) * int(self.session_price)
        return str(total_value)

    def get_session_price(self):
        return NumberTranslator().numberToString(self.session_price)

    def get_session_quantity(self):
        return NumberTranslator().translateNumber(self._session_quantity)

    def get_session_days_into_list(self):
        session_days = self._session_days
        text = ""
        for idx, day in enumerate(session_days):
            text += f'{day:0>5}'
            if idx != len(session_days) - 2:
                text += ", "
            elif idx != len(session_days) - 1:
                text += " e "

        return text
