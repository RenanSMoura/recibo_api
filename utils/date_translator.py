from datetime import datetime

months = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
          9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}


def getDateInString(**kwargs):
    if not kwargs.get('day'):
        date = datetime.now()
    else:
        date = datetime.fromtimestamp(kwargs.get('day') / 1000.0)

    day = date.day
    month = date.month

    year = date.year

    return f"São Paulo, {day} de {months[month]} de {year}"


def get_file_name(user_name: str):
    replace = user_name.replace(" ", "_")
    data = datetime.now()
    year = data.year
    month = months[data.month]

    return f'{replace}_{year}_{month}'
