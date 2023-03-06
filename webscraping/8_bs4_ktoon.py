import requests
from bs4 import BeautifulSoup

url = "https://myktoon.com/web/webtoon/works_list.kt"
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

res = requests.get(url, header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("li", attrs={"class": "tm7"})

for cartoon in cartoons:
    title = cartoon.find("strong").get_text()
    link = cartoon.find("a", attrs={"class": "link"})["href"]
    likes = cartoon.find("span", attrs={"class": "like"}).em.get_text()
    print(f"제목 : {title}\t\t좋아요 : {likes}\t\t링크 : {link}")




