from selenium.webdriver import ActionChains
from Deta.base_test_case import BaseTestCase
from Deta.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logger = Logger().getlog()


class Web_test_login(BaseTestCase):

    # 打开网址
    def open_web(self, url):
        try:
            self.driver.get(url)
            logger.info("成功打开网站>" + url)
        except Exception as e:
            logger.error("打开网站失败>" + url, e)
            raise

    # 验证网站标题
    def browser_title(self, Title):
        try:
            assert Title in self.driver.title
            logger.info("当前 网  站 标题 ：" + self.driver.title)
            logger.info("成功匹配预设标题 ：" + Title)
        except Exception as e:
            logger.info("当前 网  站 标题 ：" + self.driver.title)
            logger.info("匹配预设标题失败 ：" + Title)
            logger.error(e)
            raise

    def browser_current_url(self, url):
        try:
            self.assertEqual(self.driver.current_url, url)
            logger.info("当前 网  站 URL ：" + self.driver.current_url)
            logger.info("成功匹配预设URL ：" + url)
        except Exception as e:
            logger.info("当前 网  站 URL ：" + self.driver.current_url)
            logger.info("匹配预设URL失败 ：" + url)
            logger.error(e)
            raise

    # 显式等待方法
    def wait_element(self, type, element):
        wait = WebDriverWait(self.driver, 10)
        try:
            if type == "class_name":
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, element)))
            elif type == "css_selector":
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            elif type == "id":
                wait.until(EC.presence_of_element_located((By.ID, element)))
            elif type == "link_text":
                wait.until(EC.presence_of_element_located((By.LINK_TEXT, element)))
            elif type == "name":
                wait.until(EC.presence_of_element_located((By.NAME, element)))
            elif type == "partial_link_text":
                wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element)))
            elif type == "tag_name":
                wait.until(EC.presence_of_element_located((By.TAG_NAME, element)))
            elif type == "xpath":
                wait.until(EC.presence_of_element_located((By.XPATH, element)))
            logger.info("成功找到等待的元素>" + type + "：" + element)
        except Exception as e:
            logger.info("未找到等待的元素>" + type + "：" + element)
            logger.error(e)
            raise

    # 输入内容方法
    def element_input(self, type, element, content):
        try:
            if type == "class_name":
                self.driver.find_element_by_class_name(element).send_keys(content)
            elif type == "css_selector":
                self.driver.find_element_by_css_selector(element).send_keys(content)
            elif type == "id":
                self.driver.find_element_by_id(element).send_keys(content)
            elif type == "link_text":
                self.driver.find_element_by_link_text(element).send_keys(content)
            elif type == "name":
                self.driver.find_element_by_name(element).send_keys(content)
            elif type == "partial_link_text":
                self.driver.find_element_by_partial_link_text(element).send_keys(content)
            elif type == "tag_name":
                self.driver.find_element_by_tag_name(element).send_keys(content)
            elif type == "xpath":
                self.driver.find_element_by_xpath(element).send_keys(content)
            logger.info("成功在>" + element + "！输入值：" + content)
        except Exception as e:
            logger.info("未能在>" + element + "！输入值：" + content)
            logger.error(e)
            raise

    # 元素点击方法
    def element_click(self, type, element):
        try:
            if type == "class_name":
                self.driver.find_element_by_class_name(element).click()
            elif type == "css_selector":
                self.driver.find_element_by_css_selector(element).click()
            elif type == "id":
                self.driver.find_element_by_id(element).click()
            elif type == "link_text":
                self.driver.find_element_by_link_text(element).click()
            elif type == "name":
                self.driver.find_element_by_name(element).click()
            elif type == "partial_link_text":
                self.driver.find_element_by_partial_link_text(element).click()
            elif type == "tag_name":
                self.driver.find_element_by_tag_name(element).click()
            elif type == "xpath":
                self.driver.find_element_by_xpath(element).click()
            logger.info("成功点击指定元素>" + type + "：" + element)
        except Exception as e:
            logger.info("点击指定元素失败>" + type + "：" + element)
            logger.error(e)
            raise

    def Clear_text(self, type, element):
        try:
            if type == "class_name":
                self.driver.find_element_by_class_name(element).clear()
            elif type == "css_selector":
                self.driver.find_element_by_css_selector(element).clear()
            elif type == "id":
                self.driver.find_element_by_id(element).clear()
            elif type == "link_text":
                self.driver.find_element_by_link_text(element).clear()
            elif type == "name":
                self.driver.find_element_by_name(element).clear()
            elif type == "partial_link_text":
                self.driver.find_element_by_partial_link_text(element).clear()
            elif type == "tag_name":
                self.driver.find_element_by_tag_name(element).clear()
            elif type == "xpath":
                self.driver.find_element_by_xpath(element).clear()
            logger.info("成功清除指定元素>" + type + "：" + element)
        except Exception as e:
            logger.info("清除指定元素失败>" + type + "：" + element)
            logger.error(e)
            raise

    def Simulated_sliding(self, element):
        button = self.driver.find_element_by_id(element)  # 找到“蓝色滑块”
        action = ActionChains(self.driver)  # 实例化一个action对象
        action.click_and_hold(button).perform()  # perform()用来执行ActionChains中存储的行为
        action.reset_actions()
        action.move_by_offset(260, 0).perform()  # 移动滑块
        Web_test_login.wait_element(self, "class", "nc_iconfont btn_ok")
