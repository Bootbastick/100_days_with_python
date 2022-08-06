from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

MAX_CLICKS_PER_FIVE_MINS = 132 * 60
MAX_CLICKS_PER_FIVE_SECS = 132

chrome_driver_path = "C:/Users/NikAndSenya/nikita/python/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

the_cookie = driver.find_element(By.ID, "cookie")
cursor_cost = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').get_attribute('innerHTML').split(">")[2].replace(" ", "").replace(",", "")
grandma_cost = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').get_attribute("innerHTML").split(">")[2].replace(" ", "").replace(",", "")
factory_cost = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').get_attribute("innerHTML").split(">")[2].replace(" ", "").replace(",", "")
mine_cost = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b').get_attribute("innerHTML").split(">")[2].replace(" ", "").replace(",", "")
shipment_cost = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b').get_attribute("innerHTML").split(">")[2].replace(" ", "").replace(",", "")
alchemy_lab_cost = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').get_attribute("innerHTML").split(">")[2].replace(" ", "").replace(",", "")
portal_cost = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b').get_attribute("innerHTML").split(">")[2].replace(" ", "").replace(",", "")
time_machine_cost = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').get_attribute("innerHTML").split(">")[2].replace(" ", "").replace(",", "")

prices = [int(cursor_cost), int(grandma_cost), int(mine_cost), int(shipment_cost), int(alchemy_lab_cost), int(portal_cost), int(time_machine_cost)]

several_secs_passed_timer = 0

five_mins_passed_timer = 0

multiplayer = 1

while True:
    increasing_time = (MAX_CLICKS_PER_FIVE_SECS * multiplayer).__ceil__()
    while several_secs_passed_timer < increasing_time:
        the_cookie.click()
        several_secs_passed_timer += 1
    several_secs_passed_timer = 0
    # Adding 5 secs to 5 mins time.
    five_mins_passed_timer += MAX_CLICKS_PER_FIVE_SECS
    oneThreeTwo_clicks_aka_five_secs_passed = 0

    try:
        cookies_rn = int(driver.find_element(By.ID, "money").get_attribute("innerHTML"))
    except ValueError:
        cookies_rn = int(driver.find_element(By.ID, "money").get_attribute("innerHTML").replace(",", ""))

    for price in prices[::-1]:
        if price <= cookies_rn:
            most_expensive_affordable_thing = price
    cursor = driver.find_element(By.ID, "buyCursor")
    grandma = driver.find_element(By.ID, "buyGrandma")
    factory = driver.find_element(By.ID, "buyFactory")
    mine = driver.find_element(By.ID, "buyMine")
    shipment = driver.find_element(By.ID, "buyShipment")
    alchemy_lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
    portal = driver.find_element(By.ID, "buyPortal")
    time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
    things = [cursor, grandma, mine, shipment, alchemy_lab, portal, time_machine]

    things[prices.index(most_expensive_affordable_thing)].click()

    if five_mins_passed_timer == MAX_CLICKS_PER_FIVE_MINS:
        print(driver.find_element(By.ID, "cps").get_attribute("innerHTML"))
        five_mins_passed_timer = 0

    multiplayer += 0.1
