from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "my email"
PASSWORD = "my password"

chrome_driver_path = "C:/Users/NikAndSenya/nikita/python/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/login")

time.sleep(5)

email_bar = driver.find_element(By.ID, "username")
email_bar.click()
email_bar.send_keys(EMAIL)

password_bar = driver.find_element(By.ID, "password")
password_bar.click()
password_bar.send_keys(PASSWORD)
password_bar.send_keys(Keys.ENTER)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3198005638&f_AL=true&geoId=100733275&keywords=python%20developer&location=Montenegro&refresh=true")

messaging_hide_arrow = driver.find_element(By.XPATH, '//*[@id="ember128"]')
time.sleep(0.5)
messaging_hide_arrow.click()

jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")
print(jobs)

# save_job_buttons = driver.find_elements(By.CLASS_NAME, "jobs-save-button")
save_job_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
print(save_job_button)

the_page_list_of_jobs = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[1]/div/ul')

for job in jobs:
    job.click()
    time.sleep(0.5)
    save_job_buttons = driver.find_elements(By.CLASS_NAME, "jobs-save-button")
    that_jobs_save_button = save_job_button
    time.sleep(2)
    that_jobs_save_button.click()
    time.sleep(2)
    notification_x_button = driver.find_element(By.CLASS_NAME, "artdeco-toast-item__dismiss")
    notification_x_button.click()
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, 794)")
