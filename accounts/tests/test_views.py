from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class Test_view(LiveServerTestCase):
    def setUp(self):
        # option = FireOptions()
        option = FirefoxOptions()
        option.add_argument("--headless")
        self.driver = webdriver.Firefox(options=option,
                                        executable_path="C:/Users/user/Downloads/compresed/files/core/tests"
                                                        "/geckodriver.exe")

    def tearDown(self):
        self.driver.quit()

    def test_signin(self):
        self.driver.get('http://127.0.0.1:8000/accounts/')
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('user')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('123')
        self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()
        self.assertEqual("http://127.0.0.1:8000/file_view/", self.driver.current_url)

    def test_log_out(self):
        self.driver.get('http://127.0.0.1:8000/accounts/')
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('user')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('123')
        self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()
        self.driver.find_element(By.XPATH, "// *[ @ id = 'main-menu-navigation'] / li[2] / a").click()
        self.assertEqual("http://127.0.0.1:8000/accounts/", self.driver.current_url)




