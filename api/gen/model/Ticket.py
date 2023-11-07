from . import User
from ..utils.date_helper import get_day_month_and_year, format_date_in_payment_description


class Ticket:

    def __init__(self, user: User, **kwargs):
        self.final_text: str = kwargs.get("final_text")
        self._user = user
        self.default_ticket_directory = "recibos"

    def get_payment_date(self):
        return format_date_in_payment_description(self._user.payment_day)

    def get_file_name(self):
        user_name = self._user.name.lower()
        user_id = self._user.id
        payment_date = self._user.payment_day
        name_formatted = user_name.lower().replace(" ", "_")
        payment_day, payment_month, payment_year = get_day_month_and_year(payment_date)
        return f"{self.default_ticket_directory}/{user_id}/{payment_year}/{payment_month}/{name_formatted}_{payment_year}_{payment_month}"
