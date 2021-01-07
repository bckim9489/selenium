from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r'C:\\chromedriver.exe')
driver.implicitly_wait(10)

driver.get('http://localhost:8080/KAC_WEB/')
print(driver.title)

#Sin 1 로그인 테스트
elm_id = driver.find_element_by_id('user_id')
elm_pw = driver.find_element_by_id('pwd')
btn_elm = driver.find_element_by_id('login')

elm_id.send_keys('wkacadm')
elm_pw.send_keys('1')
btn_elm.click()

#상황정보
elm_menu = driver.find_element_by_css_selector("#gnb > ul > li:nth-child(1) > a")
action_chain = webdriver.ActionChains(driver).move_to_element(elm_menu)
action_chain.perform()
sleep(1)

#   > 상황정보조회
driver.find_element_by_css_selector("#gnb > ul > li:nth-child(1) > ul > li:nth-child(1) > a").click()

#       > 검색 테스트 (1. 셀렉트박스1 -> 캘린더(분기설정) -> 셀렉트박스2 -> 샐렉트박스3 -> 검색버튼)
select = Select(driver.find_element_by_id("srch_arprt_id")) #셀렉트 박스 목록 접수공항
select_2 = Select(driver.find_element_by_id("srch_sittn_se_code1")) #셀렉트 박스 목록 상황유형 1
select_3 = Select(driver.find_element_by_id("srch_sittn_se_code2")) #셀렉트 박스 목록 상황유형 2

size_of_select_options = len(select.options) #Option 갯수 = 반복횟수
size_of_select_2_options = len(select_2.options) #Option 갯수 = 반복횟수
btn_search = driver.find_element_by_class_name('btn_scrch')

#[xxx]DatePicker 추가 안함
for i in range(size_of_select_options):
    select.select_by_index(i) #select option 설정
    for j in range(size_of_select_2_options):
        select_2.select_by_index(j) #select option 설정
        size_of_select_3_options = len(select_3.options) #Option 갯수 = 반복횟수
        for k in range(size_of_select_3_options):
            select_3.select_by_index(k) #select option 설정
            btn_search.click()
            sleep(0.1)

sleep(5)
driver.quit()