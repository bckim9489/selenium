from selenium import webdriver
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
driver.find_element_by_css_selector("#gnb > ul > li:nth-child(1) > ul > li:nth-child(1) > a").click()
#   > 상황정보조회 (1. 셀렉트박스, 2. 캘린더, 3. 버튼,  4. 테이블 값, 5. 페이지네이션)
#       > 검색 테스트 (1. 셀렉트박스1 -> 캘린더(분기설정) -> 셀렉트박스2 -> 샐렉트박스3 -> 검색버튼)






sleep(5)
driver.quit()