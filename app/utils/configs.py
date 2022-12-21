from bs4 import BeautifulSoup
import requests

URL = "https://www.dsebd.org/old_news.php?inst=ACI&criteria=3&archive=news"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("table", class_="table-news")
news_list = results.find_all("td")