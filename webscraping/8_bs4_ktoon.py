import requests
from bs4 import BeautifulSoup

url = "https://myktoon.com/web/webtoon/works_list.kt"
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

res = requests.get(url, header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("div", attrs={"class": "info"})
total_lieks = 0

for cartoon in cartoons:
    likes = cartoon.find("span", attrs={"class": "like"}).get_text()
    print(cartoon.strong.get_text() + "\t\t좋아요: " + likes)


