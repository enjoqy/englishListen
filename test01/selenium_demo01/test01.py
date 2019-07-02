from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'http://www.en8848.com.cn/kouyu/basic/yuanlai/218414.html'
chromedriver_path = 'H:\\ChromeDownloads\chromedriver_win32\chromedriver.exe'

options = webdriver.ChromeOptions()
# 不加载图片,加快访问速度
# options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
# 超时等待5s
wait = WebDriverWait(driver, 5)
driver.get(url)
print(driver.current_url)
# 鼠标移动到某处单击
action2 = driver.find_element_by_xpath(r'//*[@id="jp_container_1"]/div[2]/div[2]/ul/li[5]/span')
ActionChains(driver).move_to_element(action2).click(action2).perform()
# 获取当前url
print(driver.current_url)
# 关闭浏览器
driver.quit()



