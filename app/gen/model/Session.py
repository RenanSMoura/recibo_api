from app.gen.utils.format_number_helper import numberToString, translateNumber
from app.gen.utils.date_helper import format_date_in_payment_description


class Session:

    def __init__(self, price, days):
        self._price = price
        self._days = days
        self._quantity = len(days)

    def get_full_session_price_description(self):
        total_value = self.get_session_total_value()
        return numberToString(str(total_value))

    def get_session_total_value(self):
        total_value = int(self._quantity) * int(self._price)
        return str(total_value)

    def get_session_price(self):
        return numberToString(self._price)

    def get_session_quantity(self):
        return translateNumber(self._quantity)

    def get_session_days_into_list(self):
        session_days = self._days
        text = ""
        for idx, day in enumerate(session_days):
            text += f'{day:0>5}'
            if idx != len(session_days) - 2:
                text += ", "
            elif idx != len(session_days) - 1:
                text += " e "

        return text
