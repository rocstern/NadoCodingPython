import requests
from bs4 import BeautifulSoup

url = "https://v2.myktoon.com/web/works/list.kt?worksseq=66"
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

res = requests.get(url, header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(res.text)

ul_toon_list = soup.find("ul", attrs={"class": "toon_lst col1 toon_lst"})
print(ul_toon_list)

# 자바스크립트를 사용한 동적인 페이지 로딩 방식을 사용하기 때문에 처음 긁어온 HTML 내용에 해당 정보가 없다
# 동적인 정보를 크롤링 하기 위해선 selenium을 사용해야 한다
episodes = ul_toon_list.find_all("li")
print(ul_toon_list.get("li"))

for episode in episodes:
    print(episode)



