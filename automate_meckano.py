#!/usr/bin/python3
import json
from selenium import webdriver
import time
import sys
import os
import platform

config_path = os.path.join(sys.path[0], 'meckano.json')
# Get access parameters
with open(config_path) as data_file:
    data = json.load(data_file)
    username = data.get('username')
    password = data.get('password')
    task = data.get('task')

if platform.system() == "Linux":
    chromedriver_path = os.path.join(sys.path[0], 'chromedriver')
elif platform.system() == "Windows":
    chromedriver_path = os.path.join(sys.path[0], 'chromedriver.exe')
else:
    chromedriver_path = ""

driver = webdriver.Chrome(chromedriver_path)
driver.implicitly_wait(5)
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
        except:
            pass
        time.sleep(1)
        driver.find_element_by_css_selector(".task-selector").click()
        driver.find_element_by_link_text(new_task).click()
        # Start new task
        try:
            driver.find_element_by_id("start-task").click()
        except:
            pass


try:
    driver.find_element_by_id("checkin-button").click()
except:
    pass

# Check for parameter containing new task or logout argument
if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg == "logout":
        try:
            driver.find_element_by_id("stop-task").click()
            time.sleep(2)
        except:
            pass

        try:
            driver.find_element_by_id("checkout-button").click()
            time.sleep(2)
        except:
            pass

        driver.close()
        # os.system("systemctl suspend")
        exit()
    else:
        update_task(arg)

# If no task provided on command line use default task from config
else:
    update_task(task)

time.sleep(2)
driver.close()
