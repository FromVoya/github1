import datetime


def solution() -> str:
    """
        Function for solution users.
        :return time_of_day:str-greeting by time of day
        """
    time = datetime.datetime.now().hour
    time_of_day = " "
    if 0 <= time < 6 or 21 <= time <= 23:
        time_of_day = "Доброй ночи"
    elif 6 <= time < 10:
        time_of_day = "Доброе утро"
    elif 10 <= time < 16:
        time_of_day = "Добрый день"
    elif 16 <= time < 21:
        time_of_day = "Добрый день"
    return time_of_day
