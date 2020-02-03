from selenium import webdriver
import os
import time

class ZalandoBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://www.zalando-lounge.pl/#/login')

    def login(self):
        email = self.driver.find_element_by_id('form-email')
z_bot = ZalandoBot('patryk', '')
