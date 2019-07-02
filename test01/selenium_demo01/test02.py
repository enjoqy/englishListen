from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'http://www.en8848.com.cn/kouyu/basic/yuanlai/218414.html'
chromedriver_path = 'H:\\ChromeDownloads\chromedriver_win32\chromedriver.exe'

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver1 = webdriver.chrome(chromedriver_path, options)

driver1.get(url)
xpath = driver1.find_element_by_xpath(r'//*[@id="jp_container_1"]/div[2]/div[2]/ul/li[5]/span')
for x in xpath:
    print(x)
