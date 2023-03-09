import requests
from bs4 import BeautifulSoup
import re
import time

start_time = time.time()

for year in range(2013, 2023):

    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for index, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]

        # https: 가 없는 링크가 생겨 추가
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        # print(f"{index} : {image_url}")
        image_res = requests.get(image_url)
        image_res.raise_for_status()


        with open(f"C:\\Workspace\\NadoCodingPython\\webscraping\\images\\movie_{year}_{index + 1}.jpg", "wb") as file:
            file.write(image_res.content)

        if index >= 4:
            break




