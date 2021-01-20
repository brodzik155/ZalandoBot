from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

categories = '//*[@id="inner-wrapper"]/section/div[2]/nav/a[1]/div'
credentials_validate = '//*[@id="react-root-form"]/div/div/div[4]/div/form/fieldset/button'
passwd = '//*[@id="form-password"]'
log = '//*[@id="form-email"]'
max_price_value = '200'


class ZalandoBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.full_size())
        self.driver.get('https://www.zalando-lounge.pl/#/login')

    @staticmethod
    def full_size():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return options

    def login(self):
        email = self.driver.find_element_by_xpath(log)
        email.send_keys(self.username)
        password = self.driver.find_element_by_xpath(passwd)
        password.send_keys(self.password)
        submit = self.driver.find_element_by_xpath(credentials_validate)
        submit.click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="inner-wrapper"]/div[1]/section/section/div').click()

    def open_companies(self, campagnies_id):
        self.driver.get('https://www.zalando-lounge.pl/campaigns/'+campagnies_id+'/all')

    def close(self):
        self.driver.quit()

    def choose_categories(self):
        self.driver.find_element_by_xpath(categories).click()
        sleep(1)
        self.driver.find_elements_by_xpath("//*[contains(text(), 'koszulki')]")[1].click()

    def price(self):
        self.driver.find_element_by_xpath('//*[@id="inner-wrapper"]/section/div[2]/nav/a[5]/div').click()
        sleep(0.5)
        input_field = self.driver.find_element_by_id('price-max')
        self.driver.execute_script("arguments[0].value = ''", input_field)
        input_field.send_keys(max_price_value)
        input_field.send_keys(Keys.RETURN)


zalando_bot = ZalandoBot()

zalando_bot.login()
sleep(2)
zalando_bot.open_companies('ZZO0V48')
sleep(2)
zalando_bot.choose_categories()
sleep(10)
