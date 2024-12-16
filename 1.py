# 确保ChromeDriver在系统PATH中或者指定其路径
# 如果在系统PATH中，可以直接调用
# driver = webdriver.Chrome()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/备用chromedriver/chromedriver')
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get('http://www.baidu.com')

# 做一些操作...

# 关闭浏览器
driver.quit()
