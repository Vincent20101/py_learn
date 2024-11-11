from selenium import webdriver
import time


test_webdriver = webdriver.Chrome()
test_webdriver.maximize_window()
#我们既可以设置浏览器的最大化，还可以设置宽和高
#注意，设置相关的宽和高度的时候，要注意，我们想要定位的元素是否会显示在浏览器上
#要么设置成最大化，要么直接保持默认即可
# test_webdriver.set_window_size(480,800)
test_webdriver.get("https://www.baidu.com")
print('第一次打开百度的首页')
time.sleep(2)
test_webdriver.get('https://news.baidu.com')
print('第一次打开百度新闻页面')
time.sleep(2)
#refresh页面的是刷新
test_webdriver.refresh()
#页面刷新
time.sleep(2)
#页面的返回
test_webdriver.back()
print('退回到百度首页')
time.sleep(2)
#页面的前进
test_webdriver.forward()
print('返回到百度新闻上去')
time.sleep(2)

#id
# test_webdriver.find_element_by_id('kw').send_keys('python')
# test_webdriver.find_element_by_id('su').click()

#name和id
# test_webdriver.find_element_by_name('wd').send_keys('python')
# test_webdriver.find_element_by_id('su').click()

#classname
# test_webdriver.find_element_by_class_name('s_ipt').send_keys('python')
# test_webdriver.find_element_by_class_name('bg s_btn btnhover').click()

#xpath
# test_webdriver.find_element_by_xpath("//input[@class='s_ipt']").send_keys('python')
# test_webdriver.find_element_by_xpath("//input[@class='bg s_btn']").click()

test_webdriver.quit()
