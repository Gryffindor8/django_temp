from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time


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

    def test_1_file_add(self):
        self.driver.get('http://127.0.0.1:8000/accounts/')
        self.driver.maximize_window()
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('user')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('123')
        self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()
        # self.driver.find_element(By.XPATH, "//a[contains(text(),\'View\')]").click()
        self.driver.find_element(By.XPATH, "// *[ @ id = 'main-menu-navigation'] / li[1] / a").click()

        self.driver.find_element(By.LINK_TEXT, "Add File").click()
        self.driver.find_element(By.ID, "id_file_name").click()
        self.driver.find_element(By.ID, "id_file_name").send_keys("java3")
        self.driver.find_element(By.XPATH, "//input[@value=\'Add File to system\']").click()

    def test_2_detail(self):
        self.driver.get('http://127.0.0.1:8000/accounts/')
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('user')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('123')
        self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),\'View\')]").click()

    def test_3_file_delete(self):
        self.driver.get('http://127.0.0.1:8000/accounts/')
        self.driver.maximize_window()
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('user')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('123')
        self.driver.find_element(By.XPATH, "//input[@value=\'Login\']").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@id='form-helpers']/div[2]/div/div/div[2]/div/table/tbody/tr/td[5]/a").click()
