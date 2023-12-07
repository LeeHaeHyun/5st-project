# video-title

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

# 크롬 버전이 바뀔 때마다 자동으로 업데이트 해준다.
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

driver.get(url="https://www.youtube.com/@jocoding/videos")
driver.maximize_window()
time.sleep(3)
for i in range(0, 40):
    driver.find_element(By.TAG_NAME, "body").send_keys(
        Keys.PAGE_DOWN
    )  # 스크롤을 40번 내려 스캔한다
    time.sleep(1)

titles = driver.find_elements(By.CSS_SELECTOR, "#video-title-link")
print(titles)


# pip install openpyxl
from openpyxl import Workbook

wb = Workbook()
ws = wb.create_sheet("조코딩")
wb.remove_sheet(wb["Sheet"])
ws.append(["제목", "링크"])

for title in titles:
    print(title.text, title.get_attribute("href"))
    ws.append([title.text, title.get_attribute("href")])

wb.save("C:/devdata/조코딩.xlsx")
wb.close()
