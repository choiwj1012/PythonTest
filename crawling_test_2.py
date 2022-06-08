from selenium import webdriver
import time

query_txt = input("검색할 키워드를 입력하세요")

chrome_path = "d:/Google Drive/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = "https://naver.com"
driver.get(url)
time.sleep(1)

element = driver.find_element_by_id("query")
driver.find_element_by_id("query").click()
element.send_keys(query_txt)
element.send_keys("\n")