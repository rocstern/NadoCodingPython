import requests
import time
from bs4 import BeautifulSoup

# url = "https://comic.naver.com/webtoon"
url = "https://docs.python.org/3/library/functions.html"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}


res = requests.get(url, header)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.find("a", attrs={"class": "GlobalNavigationBar__link--WMOzG"}))
# print(soup.find("a"))

# print(soup.title.get_text()) # .get_text 전달받은 것 중 글자만 남김
# print(soup.a) # soup이 전달 받은 텍스트 중 가장 먼저 나오는 a를 가져옴
# print(soup.a.attrs) # 가장 먼저 나오는 a태그의 속성을 가져옴
# print(soup.a["href"]) # 가장 먼저 나오는 a태그의 속성중 href만 가져옴
#
# print(soup.a["href"])

# 여기까지는 페이지에 이해도가 높을때 사용할 수 있음(get)

# print(soup.find("input", attrs={"type": "submit"}))
# print(soup.find(attrs={"type": "submit"})) # 이렇게 하면 type 값이 submit 인 모든 태그를 찾음

# print(soup.find("a", attrs={"class": "reference internal"}))
# func1 = soup.find("dl", attrs={"class": "py function"})
# print(func1.get_text())

# print(func1.next_sibling) # 태그 사이에 개행정보, 줄바꿈 등이 있을 수 있어 next_sibling 한번으로 다음 태그가 안나올 수도 있다
# print(function.next_sibling.next_sibling.get_text())

# func2 = func1.next_sibling.next_sibling
#
# func3 = func2.next_sibling.next_sibling

# print(func2.text)
#
# print(func3.get_text())

# print(func1.parent)

all_func = soup.find_all("span", attrs= {"class": "pre"})

# print(all_func["title"])

# for func in all_func:
#     if func is None:
#         print("span 존재하지 않음")
#         break
#
#     print(func.get_text())


target = soup.find("span", string="tuple()")
print(target)























