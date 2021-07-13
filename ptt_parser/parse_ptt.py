from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #呼叫鍵盤操作
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from lxml import etree

#建立chrome瀏覽器驅動，無頭模式
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install())

#載入介面
driver.get("https://www.pttweb.cc/newest/all")
time.sleep(3)

for i in range(0,10):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    i += 1
    time.sleep(4)

html = driver.page_source
print(html)


driver.quit()