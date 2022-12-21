from app import db
from app.models import News
from app.utils.utils import *


def db_insert(data):
    year = year_checker(data)
    month = month_checker(data)
    eps = eps_checker(data)

    already_exist = News.query.filter_by(year=year, month=month).first()

    if already_exist:
        already_exist.eps = eps
        db.session.commit()

    else:
        news = News(year=year, month=month, eps=eps)
        db.session.add(news)
        db.session.commit()
