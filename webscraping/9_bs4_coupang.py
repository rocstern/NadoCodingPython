import re

import requests
from bs4 import BeautifulSoup

url = "https://search.shopping.naver.com/search/all?query=%EB%85%B8%ED%8A%B8%EB%B6%81&cat_id=&frm=NVSHATC"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# div_basicList_title = soup.find_all("div", attrs={"class": re.compile("^basisList_title")})
#
# for title in div_basicList_title:
#     print(title.get_text())


div_basicList_titles = soup.find_all("div", attrs={"class": re.compile("^basicList_title")})
# div_basicList_titles = soup.find_all("div", attrs={"class": "basicList_title__VfX3c"})

for title in div_basicList_titles:
    t = title.a["title"]
    print(f"상품명 : {t}")

    sib = title.next_sibling


