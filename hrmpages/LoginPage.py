from selenium.webdriver.common.by import By

from htmhelper.selenium_helper import Selenium_Helper


class LoginPage(Selenium_Helper):

    email_ele = (By.XPATH, '//input[@name="username"]')
    password_ele = (By.XPATH, '//input[@name="password"]')
    loginbtn_ele = (By.XPATH, '//button')


    def __init__(self,driver):
        super().__init__(driver)

    def login(self,username,password):
        self.webelement_enter(self.email_ele,username)
        self.webelement_enter(self.password_ele, password)
        self.webelement_click(self.loginbtn_ele)