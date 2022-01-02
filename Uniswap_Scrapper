import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Uniswap_scrapper():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    pair1 = input("Enter Token 1: ")
    pair2 = input("Enter Token 2: ")
    price_token1 = input("Enter quantity of token 1: ")
    def load_uniswap(self):
        self.driver.get("https://app.uniswap.org/#/swap")
    def select_pairs(self):
        self.select_pair1 = self.driver.find_element(By.XPATH,"(//span[@class='sc-33m4yg-9 rqVGX token-symbol-container'])[1]")
        self.select_pair1.click()
        time.sleep(0.5)
        self.search_token = self.driver.find_element(By.XPATH,"//input[@id='token-search-input']")
        self.search_token.send_keys(self.pair1)
        time.sleep(0.5)
        self.search_token.send_keys(Keys.ENTER)
        time.sleep(0.5)
        self.select_pair2 = self.driver.find_element(By.XPATH,"(//span[@class='sc-33m4yg-9 rqVGX token-symbol-container'])[2]")
        self.select_pair2.click()
        time.sleep(0.5)
        self.search_token = self.driver.find_element(By.XPATH,"//input[@id='token-search-input']")
        self.search_token.send_keys(self.pair2)
        time.sleep(0.5)
        self.search_token.send_keys(Keys.ENTER)
        time.sleep(0.5)
    def price(self):
        self.price_input_1 = self.driver.find_element(By.XPATH,"(//input[@inputmode='decimal'])[1]")
        self.price_input_1.send_keys(self.price_token1)
        old_value= None
        while True:
            self.price_input_2 = self.driver.find_element(By.XPATH, "(//input)[2]").get_attribute("value")
            while self.price_input_2 is None or self.price_input_2 == "":
                self.price_input_2 = self.driver.find_element(By.XPATH, "(//input)[2]").get_attribute("value")
            if old_value == self.price_input_2:
                pass
            else:
                old_value = self.price_input_2
                output = {
                    f'{self.pair1}' : self.price_token1,
                    f'{self.pair2}': self.price_input_2
                }
                print(output)
