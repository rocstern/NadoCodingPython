import requests
from bs4 import BeautifulSoup

url = "https://docs.python.org/3/library/functions.html"
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

res = requests.get(url, header)
res.raise_for_status()

print(res.text)

soup = BeautifulSoup(res.text, "lxml")

# class 속성이 pre 인 모든 span element 를 반환
functions = soup.find_all("span", attrs={"class": "pre"})

for func in functions:
    print(func.get_text())


