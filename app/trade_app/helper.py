import re
from app.trade_app.patterns import *


def year_checker(eps_data):
    return re.search(year_pattern, eps_data).group(0)


def month_checker(eps_data):
    for pattern in month_pattern.split('|'):
        if pattern in eps_data:
            month = pattern

            num_month = (months.index(month) + 1) * 3
            if num_month < 12:
                return '0' + str(num_month)
            return str(num_month)


def eps_checker(eps_data):
    result_up = re.search(eps_pattern_up, eps_data)
    result_down = re.search(eps_pattern_down, eps_data)
    if result_down:
        return '-' + str(result_up.group(0))
    elif result_up:
        return result_up.group(0)
