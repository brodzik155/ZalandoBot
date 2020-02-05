from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

categories = '//*[@id="inner-wrapper"]/section/div[2]/nav/a[1]/div'
credentials_validate = '//*[@id="react-root-form"]/div/div/div[4]/div/form/fieldset/button'
passwd = '//*[@id="form-password"]'
log = '//*[@id="form-email"]'

class ZalandoBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.full_size())
        self.driver.get('https://www.zalando-lounge.pl/#/login')

#BEDE PISAŁ PO POLSKU< ZEBY LATWIEJ BYŁO XD - dorobilem tutaj metode statyczną, zeby robila pełny ekran.
    #SPRAWDZONE = DZIAŁA
    @staticmethod
    def full_size():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return options
# CO DO TYCH ZMIENNYCH TO FINALNIE PIERDOLNIE SIE JAKIS SŁOWNIK I BEDZIE SOBIE WYCIAGALO ZE SŁOWNIKA ODPOWIEDNIE WARTOSĆI, JAKIE BEDA POTRZEBNE.     A CO!
    def login(self):
        email = self.driver.find_element_by_xpath(log)
        email.send_keys(self.username)
        password = self.driver.find_element_by_xpath(passwd)
        password.send_keys(self.password)
        submit = self.driver.find_element_by_xpath(credentials_validate)
        submit.click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mainNavWrapper"]/div[2]/div[2]').click()

    def open_companies(self, campagnies_id):
        self.driver.get('https://www.zalando-lounge.pl/campaigns/'+campagnies_id+'/all')

    def close(self):
        self.driver.quit()

    def choose_categories(self):
        self.driver.find_element_by_xpath(categories).click()
        time.sleep(1)   #Odtad nie działa....
        select = Select(self.driver.find_element_by_xpath(categories))
        time.sleep(1)
        select.select_by_visible_text('Spodnie')

ig_bot = ZalandoBot('nasze.zdjecia1997@gmail.com', 'kubekpatryk')
try:
    ig_bot.login()
    time.sleep(2)
    ig_bot.open_companies('ZZO0VF1')
    time.sleep(2)
    ig_bot.choose_categories()
    time.sleep(10)
except:
    ig_bot.close()