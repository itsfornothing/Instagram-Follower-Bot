import time
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

SIMILAR_ACCOUNT = "pythoncommunity"
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Keep Chrome browser open after program finishes
CHROME_OPTION = webdriver.ChromeOptions()
CHROME_OPTION.add_experimental_option("detach", True)
CHROME_OPTION.add_argument("--window-size=650,1000")


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=CHROME_OPTION)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        time.sleep(5)
        # log_in = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        # log_in.click()
        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        time.sleep(2)
        username_input.send_keys(username)
        password_input.send_keys(password, Keys.ENTER)
        time.sleep(10)

        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(4)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

        time.sleep(3)
        search_button = self.driver.find_element(by=By.XPATH, value='//span[text()="Search"]')
        search_button.click()

        time.sleep(2)
        search = self.driver.find_element(by=By.XPATH, value='//input[@placeholder="Search"]')
        search.send_keys(SIMILAR_ACCOUNT)
        search.send_keys(Keys.ENTER)

        time.sleep(5)
        Python_community = self.driver.find_element(by=By.XPATH, value='//span[text()="Python community"]')
        Python_community.click()

        time.sleep(5)

    def find_followers(self):
        followers = self.driver.find_element(by=By.XPATH, value='//span[text()="3,259"]')
        followers.click()

        time.sleep(8)
        scrollable_popup = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[1]/div/div['
                                                              '2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div')

        time.sleep(3)
        for _ in range(10):  # Adjust the range for more or less scrolling
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            time.sleep(1)

    def follow(self):
        follow_buttons = self.driver.find_element(By.CSS_SELECTOR, 'button')
        for button in follow_buttons[:15]:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
            time.sleep(1)


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
