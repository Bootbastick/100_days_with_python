from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "my email"
USERNAME = "my username"
PASSWORD = "my password"

chrome_driver_path = "C:/Users/NikAndSenya/nikita/python/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

while True:
    # Measuring the internet speed.

    driver.get("https://www.speedtest.net/")

    time.sleep(3)

    go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    go_button.click()

    time.sleep(50)

    speed_up = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
    speed_up_number = float(speed_up.get_attribute("innerHTML"))

    speed_down = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    speed_down_number = float(speed_down.get_attribute("innerHTML"))

    MESSAGE = f"Uhhhhhhhh! My internet speed is {speed_up_number}upmbps/{speed_down_number}downmbps!"
    if speed_up_number <= 2.5:
        driver.get("https://twitter.com/i/flow/login")

        time.sleep(8)

        # Logging in Twitter.
        phone_email_or_username_tab = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[1]')
        time.sleep(3)
        driver.execute_script("arguments[0].click();", phone_email_or_username_tab)
        phone_email_or_username_input = driver.find_element(By.CLASS_NAME, "r-30o5oe")
        phone_email_or_username_input.send_keys(EMAIL)

        next_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()

        time.sleep(3)

        # Twitter asks you to input username or phone number if you'll not log in fully several times.
        username_input = driver.find_element(By.CLASS_NAME, "r-30o5oe")
        username_input.send_keys(USERNAME)
        username_input.send_keys(Keys.ENTER)

        time.sleep(1)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # Typing and sending the message in Twitter.
        message_bar = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        message_bar.click()
        message_bar.send_keys(MESSAGE)
        message_bar.send_keys(Keys.ENTER)
    time.sleep(180)
