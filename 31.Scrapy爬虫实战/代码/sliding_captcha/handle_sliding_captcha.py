# 1、要找到下面的滑块
# 2、要找到验证码的控件
# 3、截一张完整的验证码图片
# 4、点击下面的滑块，图片上将会显示缺口
# 5、隐藏缺口图片
# 6、截一张带有缺口的图片
# 7、对比两张图片的不同，不同处返回的数值，即为缺口的坐标
# 8、执行滑动操作，对滑块

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from PIL import Image, ImageChops

# 你要时刻的关注浏览器的版本以及driver的版本的适配
driver = webdriver.Chrome()
driver.get(url="http://127.0.0.1:5000")
time.sleep(3)
# 找到下面的滑块
sliding_element = driver.find_element_by_id("jigsawCircle")
# 找验证码图片的控件
captcha_element = driver.find_element_by_id("jigsawCanvas")
# 截一张完整的验证码图片
captcha_element.screenshot("before.png")
# 按一下下面的滑块
action = ActionChains(driver)
# 点一下，持续，鼠标左键不放开
action.click_and_hold(sliding_element).perform()
# 出现了缺口和缺口图片，在验证码上
# 隐藏缺口图片的js代码
script = """
document.getElementById('missblock').style['visibility'] = 'hidden';
"""
# 通过driver执行JS代码
driver.execute_script(script)
captcha_element.screenshot("after.png")
image_before = Image.open("before.png").convert("RGB")
image_after = Image.open("after.png").convert("RGB")
# 执行对比操作,通过getbbox来返回不同点的坐标
diff = ImageChops.difference(image_before, image_after).getbbox()
print(diff)
# 缺口图片能够显示出来
script = """
document.getElementById('missblock').style['visibility'] = 'visible';
"""
# 通过driver执行JS代码
driver.execute_script(script)
# 执行滑动操作,执行直线操作
action.move_by_offset(diff[0]-10, 0)
# 执行相应的动作
action.release().perform()
time.sleep(3)
driver.quit()



