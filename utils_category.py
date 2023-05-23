from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from appium.webdriver.common.touch_action import TouchAction

# Setup Component
SHARE_BUTTON = "com.zhiliaoapp.musically:id/htg"
COPY_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView"
CLOSE_DIALOG = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView"
UP_BUTTON = "com.zhiliaoapp.musically:id/c2p"
RES_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView"
PROMO_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.LynxFlattenUI[15]"
BACK_BUTTON ="com.zhiliaoapp.musically:id/awz"

def driver(SERVER_APPIUM_IP, SERVER_APPIUM_PORT, desired_caps):
        global driver
        driver = webdriver.Remote(f"http://{SERVER_APPIUM_IP}:{SERVER_APPIUM_PORT}/wd/hub", desired_caps)
        return driver

def up_button(): TouchAction(driver).tap(None, 643, 1243).perform() # coordinat of up button 
    # return driver.find_element(by=AppiumBy.ID, value=f"{UP_BUTTON}").click() # Adjust with your device

def close_dialog(): 
    return driver.find_element(by=AppiumBy.XPATH, value=f"{CLOSE_DIALOG}").click() # close unnecesary dialogbox

def close_response(): 
    return driver.find_element(by=AppiumBy.XPATH, value=f"{RES_BUTTON}").click() # close response product

def close_promo(): 
    return driver.find_element(by=AppiumBy.XPATH, value=f"{PROMO_BUTTON}").click() # close layout promo

def get_link_product():
    #driver.implicitly_wait(4)
    time.sleep(2) 
    # default 3s
    # TouchAction(driver).tap(None, 506, 101).perform()
    driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON}").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=f"{COPY_BUTTON}").click()
    return driver.get_clipboard_text()

def back_button(): 
    return driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click()

#Open Product by Coordinat
def open_product_v1(CATEGORY):
    actions = TouchAction(driver)
    df = []
    xy = {172 : 580, 530 : 580, 175 : 1200, 500 : 1200}
    for i, j in xy.items():
        try: time.sleep(2.5); actions.tap(None,i,j).perform()
        except: pass
        # try: close_response()
        # except: pass
        try:
            link = get_link_product()
            print("found link : ", link)
            df.append(link)
            time.sleep(1)
            driver.back(); continue
        except: pass
        try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click()
        except: pass
    df = pd.DataFrame(df)
    df.to_csv(f'/home/krisna/github/tiktokscraping/data_april/{CATEGORY}.csv', mode='a', index=False, header=False) # Set up Folder Save File CSV
