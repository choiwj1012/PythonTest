from selenium import webdriver
import time

query_txt = input("검색할 키워드를 입력하세요")
chrome_path = "D:/Google Drive/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = "http://www.riss.kr"
driver.get(url)
time.sleep(2)

element = driver.find_element_by_id("query")
driver.find_element_by_id("query").click()
element.send_keys(query_txt)
element.send_keys("\n")
time.sleep(2)

driver.find_element_by_link_text("학위논문").click()
time.sleep(2)

from bs4 import BeautifulSoup
html_1 = driver.page_source
soup_1 = BeautifulSoup(html_1, 'html.parser')

content_1 = soup_1.find('div','srchResultListW').find_all("li")

for i in content_1 :
    print(i.get_text().replace("\n"," ").strip())
    print("\n")

import sys
f_name = input("결과를 저장할 파일 명을 쓰세요, 경로포함")
orig_stdout = sys.stdout
file = open(f_name, 'a', encoding="UTF-8")
sys.stdout = file

for i in content_1 :
    print(i.get_text().replace("\n",""))

file.close()
sys.stdout = orig_stdout

print("데이터 수집 완료, 저장 완료")







