import unittest
import time
from selenium import webdriver
import os.path
from Deta import Basic_class


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # 浏览器最大化

    def tearDown(self):
        # 截取运行结果图片
        try:
            now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            self.driver.get_screenshot_as_file((os.path.dirname(os.path.abspath('.')) + '/png/') + now + ".png")
            Basic_class.logger.info("成功保存运行结果截图>")
        except Exception as e:
            Basic_class.logger.error("保存运行结果截图失败>" % e)
        self.driver.close()
        self.driver.quit()
