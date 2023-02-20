import requests

res = requests.get("http://google.com")
print(f"응답코드 : {res.text}")

with open("mygoogle.html", "w", encoding="UTF-8") as f:
    f.write(res.text)

