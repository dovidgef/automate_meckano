#!/usr/bin/python3
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import platform
import json
from os.path import expanduser

config_path = os.path.join(sys.path[0], 'meckano.json')
# Get access parameters
with open(config_path) as data_file:
    data = json.load(data_file)
    username = data.get('username')
    password = data.get('password')
    task = data.get('task')

options = webdriver.ChromeOptions()

home_path = expanduser("~")

if platform.system() == "Linux":
    chromedriver_path = os.path.join(sys.path[0], 'chromedriver')
    # Path to selenium chrome profile
    profile_path = home_path + "/.config/google-chrome/Selenium/"
    options.add_argument("user-data-dir=" + profile_path)
elif platform.system() == "Windows":
    chromedriver_path = os.path.join(sys.path[0], 'chromedriver.exe')
    profile_path = home_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Selenium\\"
    # Path to selenium chrome profile
    options.add_argument("user-data-dir=" + profile_path)
else:
    chromedriver_path = ""

driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://app.meckano.co.il")

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("send").click()


def update_task(new_task):
    current_task = driver.find_element_by_css_selector(".description").text
    if current_task != new_task:
        # Close current task
        try:
            driver.find_element_by_id("stop-task").click()
        except (ElementNotVisibleException, NoSuchElementException):
            pass
        if new_task != 'none':
            # Wait for select box to be clickable
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.input-bg-task-selector')))
            driver.find_element_by_css_selector(".input-bg-task-selector").click()
            new_task_xpath = "//label[contains(.//span, '{}')]".format(new_task)
            wait.until(EC.element_to_be_clickable((By.XPATH, new_task_xpath)))
            driver.find_element_by_xpath(new_task_xpath).click()
            # Start new task
            try:
                driver.find_element_by_id("start-task").click()
                wait.until(EC.element_to_be_clickable((By.ID, 'stop-task')))
            except (ElementNotVisibleException, NoSuchElementException):
                pass


try:
    driver.find_element_by_id("checkin-button").click()
    wait.until(EC.element_to_be_clickable((By.ID, 'checkout-button')))
except (ElementNotVisibleException, NoSuchElementException):
    pass

# Check for parameter containing new task or logout argument
if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg == "logout":
        try:
            driver.find_element_by_id("stop-task").click()
            element = wait.until(EC.element_to_be_clickable((By.ID, 'start-task')))
        except (ElementNotVisibleException, NoSuchElementException):
            pass

        try:
            driver.find_element_by_id("checkout-button").click()
            element = wait.until(EC.element_to_be_clickable((By.ID, 'checkin-button')))
        except (ElementNotVisibleException, NoSuchElementException):
            pass

        driver.quit()

        if platform.system() == "Linux":
            print("hello")
            os.system("systemctl suspend")
        elif platform.system() == "Windows":
            os.system('%windir%\\System32\\rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        exit()
    else:
        update_task(arg)

# If no task provided on command line use default task from config
else:
    update_task(task)

driver.quit()
