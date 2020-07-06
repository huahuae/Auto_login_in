# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
time.sleep(10)
driver=webdriver.Firefox()  #环境变量条件下执行
url='http://10.96.0.155/eportal/index.jsp?wlanuserip=8e15e834666a61d7415482db98cf7a6a&wlanacname=acecd188d5ad15bcce08adbf680feae2&ssid=&nasip=241eb546b95a411d2028280bf2cc845b&snmpagentip=&mac=5df387035cf2e07c9f44ed2cd44ca31c&t=wireless-v2&url=97bcca4b4607b74e02e80da18ea91792d9dd6dcc5d2aa5a3&apmac=&nasid=acecd188d5ad15bcce08adbf680feae2&vid=204cf0a279f9a674&port=534ed273d3d929ba&nasportid=90e9ddb2fee25e8e8901d522a3e83bce415bafc04c46effbc8e9c86ef39ee626e95f49074308e44d'
#driver=webdriver.Firefox(executable_path="/home/zhangmeng/geckodriver")
driver.get(url)
time.sleep(3)
user_name = driver.find_element_by_id('username')
user_name.send_keys('191307040034')
time.sleep(1)
user_name.send_keys(Keys.TAB)
user_Id = driver.find_element_by_id('pwd')
user_Id.send_keys('110012as')
#巧用Tap键
user_Id.send_keys(Keys.TAB)
user_chice=driver.find_element_by_id('selectDisname')
user_chice.send_keys(Keys.DOWN)
user_chice.send_keys(Keys.DOWN)
time.sleep(1)
driver.find_element_by_id('_service_0').click()
time.sleep(1)
driver.find_element_by_id('loginLink_div').click()
time.sleep(100)
driver.quit()



