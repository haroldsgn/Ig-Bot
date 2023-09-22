import os
import time
import selenium

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

CHROME_DRIVER_PATH = "C:\development\chromedriver-win64\chromedriver.exe"
SIMILAR_ACCOUNT = "buzzfeedtasty"
IG_USERNAME = os.environ.get("USERNAME")
IG_PASSWORD = os.environ.get("PASSWORD")


class InstaFollower:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()

        time.sleep(5)

        user = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys(IG_USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(IG_PASSWORD)
        time.sleep(1)
        submit = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        submit.click()

        time.sleep(3)
        try:
            ig_notification = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_FV"]/div/div/div[3]/div/div/div['
                                                                 '1]/div/div[2]/div/div/div/div/div[2]/div/div/div['
                                                                 '3]/button[1]')
            ig_notification.click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        time.sleep(3)
        search_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div['
                                                           '1]/div[1]/div/div/div/div/div[2]/div[2]/span/div')
        search_button.click()

        time.sleep(3)

        search_account = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div['
                                                            '1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        search_account.send_keys(SIMILAR_ACCOUNT)

        time.sleep(5)

        select_account = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div['
                                                            '1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div['
                                                            '1]/a')
        select_account.click()

        time.sleep(15)

        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div['
                                                       '1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

    def follow(self):

        time.sleep(5)

        all_follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.x1dm5mii button')
        for button in all_follow_buttons:
            try:
                button.click()
                time.sleep(3)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div[2]/div['
                                                                   '1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

