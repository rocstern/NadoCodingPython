import requests
import re
from bs4 import BeautifulSoup

url = "https://prod.danawa.com/list/?cate=112758&shortcutKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(res.text)



# 상품 목록 글어오기
item_list = soup.find_all("li", attrs={"class": "prod_item prod_layer"})


for item in item_list:

    # 상품 이름
    item_name = item.find("a", attrs={"name": "productName"})
    if not item_name:
        print("상품 이름 정보가 없음\n")
        continue

    item_name = item_name.get_text().strip()

    # 상품 가격 class=price_sect 가진 <p> 태그 자손 중 <strong> 태그 값 가져오기
    item_price = item.find("p", attrs={"class": "price_sect"})
    if not item_price:
        print("상품 가격 정보가 없음1\n")
        continue
    item_price = item_price.find("strong")
    if not item_price:
        print("상품 가격 정보가 없음2\n")
        continue

    item_price = item_price.get_text().strip()
    item_price = item_price.replace(",", "")

    # 상품 평가 //*[@id="productItem17980256"]/div/div[2]/div[3]/div/dl[2]/dd/a/strong
    # 이유는 몰라도 다나와에서 평가 정보가 나오는 <dl class="meta_item mt_comment> 태그 requests 를 막아놨다
    # item_review = item.find("dl", attrs={"class": "mt_comment"})
    # if not item_review:
    #     print(f"{item_name}상품 평가 정보가 없음1\n")
    #     continue
    # item_review = item_review.find("strong")
    # if not item_review:
    #     print(f"{item_name}상품 리뷰 정보가 없음2\n")
    #     continue
    #
    # item_review = item_review.get_text().strip()


    # 150만원 이상 가격이거나 평가 횟수가 10회 미만인 제품은 정보 띄우지 말고 패스
    if not item_price or int(item_price) > 1500000:
        print(f"{item_name} 가격 조건이 맞지 않음\n")
        continue
    # if not item_review or int(item_review) < 10:
    #     print(f"{item_name} 평가 조건이 맞지 않음\n")
    #     continue

    print(f"상품명:\t\t{item_name}")
    print(f"가격:\t\t{item_price}원")
    # print(f"평가횟수:\t\t{item_review}")
    print("")
    print("")

