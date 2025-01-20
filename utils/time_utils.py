import datetime


def format_time(sec: float):
    return str(datetime.timedelta(seconds=sec))[:-3]

def get_time_difference(first_moment: int, second_moment: int):
    return round(abs(first_moment - second_moment), 3)