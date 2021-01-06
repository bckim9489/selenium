from selenium import webdriver
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

elm_menu = driver.find_elements_by_css_selector("#gnb > ul > li:nth-child(1) > ul > li:nth-child(1) > a")
elm_menu[0].click()



sleep(5)
driver.quit()