import time

from bs4 import BeautifulSoup
import requests

from app.trade.utils import add_trade


def get_name(trade_code):
    URL = "https://www.dsebd.org/displayCompany.php?name={}".format(trade_code)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("h2", class_="topBodyHead")
    result = result.find("i")
    return result.decode_contents()


def get_trade():
    trade_list = []
    URL = "https://www.dsebd.org/cbul.php"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("table", class_="table")
    results = results.find_all("a", class_="ab1")

    for trade_code in results:
        trade_list.append(trade_code.decode_contents())

    return trade_list


def get_news(trade_code):
    URL = "https://www.dsebd.org/old_news.php?inst={}&criteria=3&archive=news".format(trade_code)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("table", class_="table-news")
    news_list = results.find_all("td")
    return news_list
