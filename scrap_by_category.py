from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction
from utils_category import open_product_v1, driver, close_dialog, up_button, back_button

# Setup Connection and prodruct
SESSION = 100
SCROLL_LOOP = 5
CATEGORY = "womenwear"
CONNECTION = "192.168.0.106:5555"
SERVER_APPIUM_PORT = "4723"
SERVER_APPIUM_IP = "127.0.0.1"

DESIRED_CAPS = {
    "platformName": "Android",
    "appium:deviceName": "device",
    "appium:udid": CONNECTION,
    "appium:noReset": True,
}

driver = driver(SERVER_APPIUM_IP=SERVER_APPIUM_IP, SERVER_APPIUM_PORT=SERVER_APPIUM_PORT, desired_caps=DESIRED_CAPS)

### Scroll To Product Layout
time.sleep(2)
driver.swipe(350, 1300, 350, 657, 500) # Adjust with your device
time.sleep(2)


A = 0
while A <= SESSION:
    k = 0
    while k <= SCROLL_LOOP:
        print (f"Scrape the loop at {k}")
        open_product_v1(CATEGORY=CATEGORY)
        time.sleep(2)
        driver.swipe(360, 1300, 360, 380, 400) # defautl 360, 1300, 360, 400, 400 Adjust with your device
        # try : back_button()
        # except: continue
        k = k + 1
    try: time.sleep(2); up_button()
    except: pass

    time.sleep(3)
    driver.swipe(360, 260, 360, 638, 200) # Adjust with your device
    time.sleep(6)
    driver.swipe(360, 1300, 360, 657, 500) # Adjust with your device
    A = A + 1