# 打开目标站点
# 截取全屏图片
# 获取验证码的区域，获取验证码的控件
# 截取验证码的图片
# 将验证码的图片发送给超级鹰
# 根据超级鹰返回的文字的坐标执行点击操作

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
from chaojiying import Chaojiying_Client
from setting import username, password, soft_id
from selenium.webdriver import ActionChains


class click_choice_captcha(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def handle_captcha(self):
        try:
            self.driver.get("http://127.0.0.1:5000/")
            # 监控验证码控件出现
            if WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "verify-img-panel"))):
                # 等待验证码图片加载完成
                time.sleep(2)
                # 输出两张图片，分别为整个浏览器全图和验证码区域图片
                captcha_element = self.save_img()
                if captcha_element:
                    # 获取到超级鹰识别的验证码结果
                    nodes = self.handle_chaojiying()
                    if nodes:
                        print("验证码识别成功，开始点击验证码")
                        for i in nodes.split("|"):
                            # 执行点击操作
                            ActionChains(self.driver).move_to_element_with_offset(captcha_element, int(i.split(",")[0]), int(i.split(",")[1])).click().perform()
                            time.sleep(1)
        except Exception as e:
            print("验证码识别失败")
            self.driver.quit()
        else:
            time.sleep(2)
            self.driver.quit()

    def handle_chaojiying(self):
        """验证码识别"""
        chaojiying = Chaojiying_Client(username, password, soft_id)
        # 读取验证码
        with open("captcha.png", "rb") as f:
            img = f.read()
        return_data = chaojiying.PostPic(img, 9103)
        print("超级鹰返回的验证码数据为: {}".format(return_data))
        return return_data.get("pic_str")

    def save_img(self):
        """截取图片，保存图片"""
        try:
            print("开始截图")
            # 截取全屏图片
            self.driver.save_screenshot("browser.png")
            # 找到验证码的控件
            captcha_element = self.driver.find_element_by_xpath("//img[@class='back-img']")
            # 获取验证码左上角坐标
            location = captcha_element.location
            # 获取验证码的大小，宽和高
            size = captcha_element.size
            print(location, size)
            # 验证码整张图片的大小，尺寸
            rangle = (location.get("x"), location.get("y"), location.get("x")+size.get("width"), location.get("y")+size.get("height")+50)
            # 打开前面截图的全屏图片
            img = Image.open("browser.png")
            # 通过前面定义的验证码图片的大小来绘制整个验证码图片的区域
            captcha = img.crop(rangle)
            captcha.save("captcha.png")
        except Exception as e:
            return False
        else:
            # 便于后期获取到验证码坐标之后进行点击操作
            return captcha_element


if __name__ == '__main__':
    c = click_choice_captcha()
    c.handle_captcha()
