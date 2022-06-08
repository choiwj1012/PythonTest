# riss.kr에서 특정 키워드로 논문 / 학술 자료 검색하기

# Step 1. 필요한 모듈 로딩
from selenium import webdriver
import time # time 모듈은 페이지가 전부 열릴 때까지 기다려주는 명령을 사용할 수 있다. time.sleep(seconds)

# Step 2. 사용자에게 검색 관련 정보들을 입력 받습니다.
print("=" * 100)
print("이 크롤러는 RISS 사이트의 논문 및 학술자료 수집용 웹크롤러입니다.")
print("=" * 100)

query_txt = input("1. 수집할 자료의 키워드는 무엇입니까? (여러개일 경우 , 로 구분하여 입력):")
# query_txt = "해양자원, 도시재생"
print("\n")

# Step 3. 크롬 드라이버 설정 및 웹 페이지 열기
chrome_path = "d:/Google Drive/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

url = "http://www.riss.kr"
driver.get(url)
time.sleep(2)

# Step 4. 자동으로 검색어 입력 후 조회하기
element = driver.find_element_by_id("query")
driver.find_element_by_id("query").click()
element.send_keys(query_txt)
element.send_keys("\n")

# find_element_by_id(`html_id`)
# find_element_by_name(`html_name`)
# find_element_by_xpath(`/html/body/some/xpath')
# find_element_by_css_selector(`#css > div.selector')
# find_element_by_tag_name(`h1`)
# find_element_by_link_text(`텍스트이름`)


