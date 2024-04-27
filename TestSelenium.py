from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('detach', True)
s = Service('D:/BeautifulSoup/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service= s,options=options) 
# driver.get('https://www.bgsu.edu/') 
# time.sleep(4)
# driver.find_element('xpath',"/html/body/div[5]/div[2]/nav/div/div[2]/ul/li[8]/a[1]").click()
# driver.get('https://www.google.com/')
# search =driver.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
# search.send_keys("best university")
# search.send_keys(Keys.ENTER) 
driver.get('https://webparanoid.com/en') 
driver.find_element('xml','/html/body/div/div/div[1]/div/label/input').click()
# driver.save_screenshot('D:/BeautifulSoup/webpranoid.png')
time.sleep(3)
driver.find_element('xml','/html/body/div/button').click()
driver.find_element('xml','/html/body/main/section[1]/div/div')
driver.save_screenshot('D:/BeautifulSoup/nav_bar.png')