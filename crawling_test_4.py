from selenium import webdriver
import time

query_txt = "moneynlifehacker.com"
chrome_path = "D:/Google Drive/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = "https://naver.com"
driver.get(url)
time.sleep(2)

element = driver.find_element_by_id("query")
driver.find_element_by_id("query").click()
element.send_keys(query_txt)
element.send_keys("\n")
time.sleep(2)

driver.find_element_by_link_text("VIEW").click()
time.sleep(2)

from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
content = soup.find('ul',"lst_total").find_all("li")

import sys
f_name = "d:/navertest.txt"
orig_stdout = sys.stdout
file = open(f_name, 'a', encoding="UTF-8")
sys.stdout = file

for i in content :
    print(i.get_text().replace("\n",""))

file.close()
sys.stdout = orig_stdout



