import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "account you want to follow the followers of"
USERNAME = "username"
PASSWORD = "password"

chrome_driver_path = "chrome driver path"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self, username: str, password: str):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username_bar = self.driver.find_element(By.NAME, "username")
        username_bar.click()
        username_bar.send_keys(username)
        password_bar = self.driver.find_element(By.NAME, "password")
        password_bar.click()
        password_bar.send_keys(password)
        password_bar.send_keys(Keys.ENTER)

    def find_followers(self, account_to_follow_from: str):
        search_bar = self.driver.find_element(By.CLASS_NAME, 'XTCLo')
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", search_bar)
        search_bar.send_keys(account_to_follow_from)
        time.sleep(1)
        first_account_found = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        needed_account = first_account_found
        needed_account.click()
        time.sleep(5)
        followers_buttons = self.driver.find_elements(By.CLASS_NAME, '_aacx')
        followers_buttons[3].click()

    def follow(self):
        followers = self.driver.find_elements(By.CLASS_NAME, '_acan')
        print(len(followers))
        for follower in followers[3::]:
            self.driver.execute_script("arguments[0].click();", follower)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       follower)
            time.sleep(1)


bot = InstaFollower(chrome_driver_path)
bot.login(USERNAME, PASSWORD)
time.sleep(5)
bot.find_followers(SIMILAR_ACCOUNT)
time.sleep(6)
bot.follow()
