import requests
from bs4 import BeautifulSoup
import csv
import re
import time

start_time = time.time()

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

for page in range(1, 5):

    res = requests.get(url + str(page))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")


    table = soup.find("table", attrs={"class": "type_2"})

    stocks = table.find_all("tr", attrs={"onmouseover": "mouseOver(this)"})

    if not stocks:
        print("stocks is None")

    for idx, stock in enumerate(stocks):
        index = 25 * (page - 1) + idx

        stock_name = stock.find("a", attrs={"class": "tltle"})
        if not stock_name:
            continue
        stock_name.get_text()


        stock_current_value = stock.find("td", attrs={"class": "number"})
        if not stock_current_value:
            continue
        # stock_current_value = stock_current_value.get_text()

        vs_yesterday = stock_current_value.next_sibling.next_sibling

        ratio = vs_yesterday.next_sibling

        print("현재가: ", stock_current_value)
        print("전일비: ", vs_yesterday)
        print("등락률: ", ratio)






