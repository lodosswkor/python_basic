from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.parse   
import time

options = webdriver.ChromeOptions() 
#options.add_argument("headless")
options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")
driver = webdriver.Chrome(options)

url_template = 'https://search.danawa.com/dsearch.php?query={0}&sort=opinionDESC' 
now_page = 1
max_page = 10 

while True : 
    
    search_text = input("검색할 제품을 입력해 주세요 (종료 q) : ")    
    if search_text == 'q' :
        break 

    url = url_template.format(search_text) 
    
    driver.get(url) 
    pages = driver.find_elements(By.XPATH, '//*[@id="paginationArea"]/div/div/a') 
    
    max_page = len(pages)
    if max_page < 1 :
        print("검색된 데이터가 없습니다.")
        continue
    
    # paging 처리 확인
    product_names = driver.find_elements(By.CLASS_NAME, 'click_log_product_standard_title_')
    print("갯수 : %s" %(len(product_names)))
    
    for name in product_names :
        print(name.text)
        
    pages[idx + 1].click()    
    time.sleep(3)

    
print('프로그램 종료')

# driver.get("https://prod.danawa.com/list/?cate=112758&shortcutKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81")
# notebook_names = driver.find_elements(By.CSS_SELECTOR, '[name="productName"]')

    
# btn_pagings = driver.find_elements(By.XPATH, '//*[@id="productListArea"]/div[6]/div/div/a')
# for page_num in btn_pagings :
#     print(page_num.text)


