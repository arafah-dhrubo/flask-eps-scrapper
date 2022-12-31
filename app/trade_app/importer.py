import re
import time
from termcolor import cprint
from app.models import Trade
from app.trade_app.patterns import pattern
from app.trade_app.soup import get_news, get_trade
from app.trade_app.utils import add_trade, add_news


def convert(seconds):
    return time.strftime("%M:%S", time.gmtime(seconds))


def import_trades():
    seconds = 0
    completed = 0
    sleep_time = 0.05
    trade_list = get_trade()
    for trade_code in trade_list:
        add_trade(trade_code)
        import_eps(trade_code)
        print("Importing EPS For " + trade_code + ' Done ✅ ')
        time.sleep(sleep_time)
        seconds += sleep_time
        completed += 1
        cprint("Completed {} Trades in {} minutes".format(completed, round(seconds)), 'green')


def import_eps(trade_code):
    trade_id = Trade.query.filter_by(trade_code=trade_code).first().id
    for news in get_news(trade_code):
        text = news.text.strip()

        if re.search(pattern, text):
            raw_data = text.split(':')[1].split(';')[0]
            if 'against' in raw_data:
                current = raw_data.split('against')[0]
                previous = raw_data.split('against')[1]

                add_news(current, trade_id)
                add_news(previous, trade_id)
