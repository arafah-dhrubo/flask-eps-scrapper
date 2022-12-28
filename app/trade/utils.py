from app import db
from app.models import News, Trade
from app.trade.helper import *


def add_news(data, trade_id):
    year = year_checker(data)
    month = month_checker(data)
    eps = eps_checker(data.replace(" ", ""))

    already_exist = News.query.filter_by(year=year, month=month, trade_id=trade_id).first()

    if already_exist:
        already_exist.eps = eps
        db.session.commit()

    else:
        news = News(year=year, month=month, eps=eps, trade_id=trade_id)
        db.session.add(news)
        db.session.commit()


def add_trade(trade_code):
    already_exist = Trade.query.filter_by(trade_code=trade_code).first()
    if not already_exist:
        trade = Trade(trade_code=trade_code)
        db.session.add(trade)
        db.session.commit()
        db.session.flush()
        return trade.id

