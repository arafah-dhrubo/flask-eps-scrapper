from flask import render_template, redirect, url_for
from app import app
from app.models import News
from app.utils.configs import news_list
from app.utils.refresher import db_insert
from app.utils.utils import *


@app.route('/')
def index():
    newses = News.query.order_by(News.year.desc(), News.month.desc()).all()
    return render_template('index.html', news_list=newses)


@app.route('/refresh')
def refresh():
    for news in news_list:
        text = news.text.strip()

        if re.search(pattern, text):
            raw_data = text.split(':')[1].split(';')[0]
            current = raw_data.split('against')[0]
            previous = raw_data.split('against')[1]

            db_insert(current)
            db_insert(previous)
    return redirect(url_for('index'))
