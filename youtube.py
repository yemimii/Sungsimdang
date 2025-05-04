# 유튜브 영상 제목 크롤링
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def scroll_and_extract_titles1(driver, scrolls=20, delay=2):
    titles_set = set()  # 중복을 방지하기 위해 집합 사용
    for _ in range(scrolls):
        # 현재 페이지의 제목들을 수집
        titles = driver.find_elements(By.CSS_SELECTOR, 'h3 a')
        for title in titles:
            titles_set.add(title.text)

        # 페이지 끝까지 스크롤
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(delay)  # 새로운 컨텐츠 로딩을 위해 잠시 대기

    return titles_set


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

# 유튜브 검색 페이지 열기
url = 'https://www.youtube.com/results?search_query=%EC%84%B1%EC%8B%AC%EB%8B%B9'
driver.get(url)

# 페이지 로딩 대기
time.sleep(5)

# 스크롤하면서 제목 추출
extracted_titles = scroll_and_extract_titles1(driver, scrolls=20, delay=2)

# 추출된 제목 출력
for title in extracted_titles:
    print(title)

driver.quit()  # 브라우저 종료
