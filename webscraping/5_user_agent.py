import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"}

res = requests.get(url, headers=headers)
res.raise_for_status()

with open("novelpiatest.html", "w", encoding="UTF8") as f:
    f.write(res.text)