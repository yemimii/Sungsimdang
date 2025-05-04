from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta

def scroll_and_extract_titles_and_dates(driver, scrolls=50, delay=2):
    titles_and_dates_list = []  # 중복을 방지하기 위해 리스트 사용
    for _ in range(scrolls):
        # 네이버 뉴스의 기사 제목들과 날짜를 수집
        news_items = driver.find_elements(By.CSS_SELECTOR, 'div.news_area')
        for item in news_items:
            title = item.find_element(By.CSS_SELECTOR, 'a.news_tit').text
            date_ornot = item.find_elements(By.CSS_SELECTOR, 'span.info')
            if len(date_ornot) >= 2:
                date = date_ornot[1].text
                titles_and_dates_list.append((title, date))
            else:
                date = date_ornot[0].text
                titles_and_dates_list.append((title, date))

        # 페이지 끝까지 스크롤
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(delay)  # 새로운 컨텐츠 로딩을 위해 잠시 대기

    # 날짜를 기준으로 정렬
    titles_and_dates_list.sort(key=lambda x: parse_date(x[1]) or datetime.min, reverse=True)

    # 추출된 제목과 날짜 출력
    for title, date in titles_and_dates_list:
        print(f"{title} {date}")

def parse_date(date_str):
    # 날짜 형식 파싱 (예: '1시간 전', '2일 전', '2024.05.19.' 등)
    if '면' not in date_str:
        return datetime.strptime(date_str, '%Y.%m.%d.')
    else:
        return date[2] # 명시적으로 아무 것도 반환하지 않음

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

# 네이버 뉴스 검색 페이지 열기
url = 'https://search.naver.com/search.naver?where=news&query=%EC%84%B1%EC%8B%AC%EB%8B%B9&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2017.04.13&de=2019.04.13&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Afrom20160219to20180219&is_sug_officeid=0&office_category=0&service_area=0'
driver.get(url)

# 페이지 로딩 대기
time.sleep(5)

# 스크롤하면서 제목과 날짜 추출 및 출력
scroll_and_extract_titles_and_dates(driver, scrolls=50, delay=2)

driver.quit()  # 브라우저 종료
