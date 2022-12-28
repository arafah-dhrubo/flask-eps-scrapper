from flask import render_template, redirect, url_for, request
from flask.json import dump

from app import app
from app.trade.importer import import_trades
from app.trade.soup import *
from app.trade.utils import *
from app.trade.helper import *

@app.route('/import-data')
def import_data():
    return render_template('import.html')


@app.route('/importer')
def importer():
    import_trades()
    return redirect(url_for('index'))


@app.route('/')
def index():
    trades = Trade.query.all()
    trade_count = Trade.query.count()
    if trade_count == 0:
        return render_template('import.html')
    return render_template('index.html', trades=trades, trade_count=trade_count)


@app.route('/eps')
def eps():
    trade_id = request.args['trade_id']
    newses = News.query.order_by(News.year.desc(), News.month.desc()).filter_by(trade_id=trade_id)
    return render_template('eps.html', news_list=newses, trade_id=trade_id)
