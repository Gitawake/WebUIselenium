from Deta.Basic_class import Web_test_login
import time


class login(Web_test_login):

    def test_login(self):
        Web_test_login.open_web(self, "http://cloud.uc.cn/")
        Web_test_login.browser_title(self, "UC云_云存储,云同步,云下载,云加速,云安全,云开放_UC浏览器官网")
        Web_test_login.wait_element(self, "id", "btn_login")
        Web_test_login.element_input(self, "id", "login_name", "444444")
        Web_test_login.element_click(self, "id", "password_b")
        Web_test_login.element_input(self, "id", "login_pwd", "5555")
        Web_test_login.Simulated_sliding(self, "nc_1__bg")
        time.sleep(5)
        Web_test_login.element_click(self, "id", "btn_login")
        Web_test_login.wait_element(self, "class", "out")
        Web_test_login.element_click(self, "link_text", "书签")
        time.sleep(5)
        Web_test_login.browser_current_url(self, "http://bookmark.yun.uc.cn/")
        time.sleep(5)

# if __name__ == '__main__':
#     import unittest
#
#     unittest.main()
