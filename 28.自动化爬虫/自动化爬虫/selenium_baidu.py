from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



# 实例化参数的方法
chrome_options = Options()
# 设置浏览器的无头浏览器，无界面,浏览器将不提供界面，linux操作系统无界面情况下就可以运行了
chrome_options.add_argument("--headless")
# 结果devtoolsactiveport文件不存在的报错
chrome_options.add_argument("--no-sandbox")
# 官方推荐的关闭选项，规避一些BUG
chrome_options.add_argument("--disable-gpu")
# 实例化了一个chrome,导入设置项
test_webdriver = webdriver.Chrome(options=chrome_options)
# 最大化
test_webdriver.maximize_window()
# 打开百度
test_webdriver.get("https://www.baidu.com")
# 再输入框里面输入了python
test_webdriver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
# 执行了点击操作
test_webdriver.find_element_by_xpath("//input[@id='su']").click()
time.sleep(2)
# 打印web界面的title
print(test_webdriver.title)
# 浏览器退出
test_webdriver.quit()