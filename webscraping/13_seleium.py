import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip


user_id = "rocstern"
user_pwd = "Asdwsx!2"

options = webdriver.ChromeOptions()
# 브라우저 닫힘 방지
options.add_experimental_option('detach', True)
# 불필요한 로그 방지
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = ChromeService(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=options)
browser.get("http://naver.com")

login_elem = browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[3]/div/div[2]/a")

# print(login_elem.get_attribute("outerHTML"))

login_elem.click()

time.sleep(5)

id_field = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[1]/input")
pwd_field = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[1]/div[2]/input")


# pyperclip id, pwd
pyperclip.copy(user_id)
id_field.send_keys(Keys.CONTROL, "v")

pyperclip.copy(user_pwd)
pwd_field.send_keys(Keys.CONTROL, "v")

time.sleep(1)

login_btn = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[7]/button")
login_btn.click()











