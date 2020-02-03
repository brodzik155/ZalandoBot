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
        email = self.driver.find_element_by_xpath('//*[@id="form-email"]')
        email.send_keys(self.username)
        password = self.driver.find_element_by_xpath('//*[@id="form-password"]')
        password.send_keys(self.password)
        click = self.driver.find_element_by_xpath('//*[@id="react-root-form"]/div/div/div[4]/div/form/fieldset/button').click()


ig_bot = ZalandoBot('nasze.zdjecia1997@gmail.com', 'kubekpatryk')
ig_bot.login()