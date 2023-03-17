import requests
from bs4 import BeautifulSoup
import csv
import re
import time

start_time = time.time()

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok1=0&page="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

file_name = "시가총액 1-200.csv"

f = open(file_name, "w", encoding="utf-8-sig", newline="")

writer = csv.writer(f)

csv_title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(csv_title)


for page in range(1, 5):

    res = requests.get(url + str(page))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")


    table = soup.find("table", attrs={"class": "type_2"})

    data_rows = table.find_all("tr", attrs={"onmouseover": "mouseOver(this)"})

    if not data_rows:
        print("stocks is None")

    for idx, row in enumerate(data_rows):

        index = 25 * (page - 1) + idx

        # stock_name = stock.find("a", attrs={"class": "tltle"})
        # if not stock_name:
        #     continue
        # stock_name.get_text()
        #
        #
        # stock_current_value = stock.find("td", attrs={"class": "number"})
        # if not stock_current_value:
        #     continue
        # # stock_current_value = stock_current_value.get_text()
        #
        # vs_yesterday = stock_current_value.next_sibling.next_sibling
        #
        # ratio = vs_yesterday.next_sibling
        #
        # print("현재가: ", stock_current_value)
        # print("전일비: ", vs_yesterday)
        # print("등락률: ", ratio)

        columns = row.find_all("td")
        data = [column.get_text().strip() for column in columns]

        # 리스트 형태로 넣으면 됨
        writer.writerow(data)






