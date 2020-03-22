from selenium import webdriver
from data import menti_code
import time
sleep_time = 1.5


class MentiBot:
    def __init__(self):
        self.driver = None
        self.options_list = []
        self.nr_of_options = 0
        self.menti_code_url = ''

    def open_menti(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome('C:/webdrivers/chromedriver', chrome_options=chrome_options)
        self.driver.get('https://menti.com')
        time.sleep(sleep_time)

    def submit_menti_code(self):
        menti_code_entry = self.driver.find_element_by_xpath('//*[@id="enter-vote-key"]')
        menti_code_entry.send_keys(menti_code)
        submit_code_btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/button')
        submit_code_btn.click()
        time.sleep(sleep_time)
        setattr(self, 'menti_code_url', self.driver.current_url)

    def reopen_menti(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome('C:/webdrivers/chromedriver', chrome_options=chrome_options)
        self.driver.get(self.menti_code_url)
        time.sleep(sleep_time)

    def vote(self, vote):
        xpath = '//*[@data-testid="choice-'
        option = self.driver.find_element_by_xpath(xpath + str(vote) + '"]')
        option.click()
        submit_code_btn = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/form/div/button')
        submit_code_btn.click()
        time.sleep(sleep_time)

    def close_driver(self):
        self.driver.close()

    def get_voting_options(self):
        xpath = '//*[@data-testid="choice-'

        nr_of_performances = 14
        for i in range(nr_of_performances):
            new_option = self.driver.find_elements_by_xpath(xpath + str(i) + '"]')
            self.options_list += new_option

        self.nr_of_options = len(self.options_list)
