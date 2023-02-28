import requests

res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")

# res.raise_for_status()
print(f"응답코드 : {res.status_code}")

# print(res.text)

with open("mygoogle.html", "w", encoding="UTF8") as f:
    f.write(res.text)