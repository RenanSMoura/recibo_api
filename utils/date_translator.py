from datetime import datetime
from pathlib import Path

months = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
          9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}


# pattern = re.compile("(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])")

def getDateInString(paymentDay: str):
    payment_day = paymentDay

    if not payment_day:
        date = datetime.now()
    else:
        date = translate_to_date_time(payment_day)

    day = date.day
    month = date.month

    year = date.year

    return f"São Paulo, {day} de {months[month]} de {year}"


def get_file_name(user_name: str):
    folder = "recibos/"
    replace = user_name.replace(" ", "_")
    data = datetime.now()
    year = data.year
    month = months[data.month + 1]
    folder_month = f"{month}/"

    Path(f"{folder}{folder_month}").mkdir(parents=True, exist_ok=True)

    return f'{folder}{folder_month}{replace}_{year}_{month}'


def translate_to_date_time(payment_day: str):
    date_time_obj = datetime.strptime(payment_day, '%d/%m/%Y')
    return date_time_obj


# date_time_obj = datetime.strptime(date_time_str, '%d/%m')
# print("The type of the date is now", type(date_time_obj))
# print("The date is", date_time_obj.month)
