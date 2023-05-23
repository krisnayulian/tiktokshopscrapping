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
CLOSE_LIVE = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView"

def driver(SERVER_APPIUM_IP, SERVER_APPIUM_PORT, desired_caps):
        global driver
        driver = webdriver.Remote(f"http://{SERVER_APPIUM_IP}:{SERVER_APPIUM_PORT}/wd/hub", desired_caps)
        return driver

def close_dialog(): return driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_DIALOG}").click() # close unnecesary dialogbox

def close_response(): 
    return driver.find_element(by=AppiumBy.XPATH, value=f"{RES_BUTTON}").click() # close response product

def get_link_product():
    #driver.implicitly_wait(4)
    time.sleep(2)
    driver.find_element(by=AppiumBy.ID, value=f"{SHARE_BUTTON}").click()
    #driver.implicitly_wait(4)
    time.sleep(1)
    driver.find_element(by=AppiumBy.XPATH, value=f"{COPY_BUTTON}").click()
    return driver.get_clipboard_text()

# Open Product by Coordinat
def open_product_v1(CATEGORY):
    actions = TouchAction(driver)
    df = []
    xy = {172 : 580, 530 : 580, 175 : 1200, 500: 1200, # Click coordinat
        #264 : 1855, 823 : 1855
        }
    for i, j in xy.items():
        try: 
            time.sleep(2); actions.tap(None,i,j).perform()
        except: 
            print("cant open the product"); continue
        try: close_response()
        except: pass
        # try: close_dialog()
        # except: pass
        time.sleep(1); driver.swipe(360, 990, 360, 1185, 400)
        try:
            link = get_link_product()
            print("found link : ", link)
            df.append(link)
            driver.back(); #continueS
            # Back Video Product
            # time.sleep(2); driver.find_element(by=AppiumBy.ID, value=f"{BACK_VIDEO}").click()
            # # Close Live
            # time.sleep(2); driver.find_element(by=AppiumBy.XPATH, value=f"{CLOSE_LIVE}").click()
        except: pass
        # try: # Close end live
        #     time.sleep(1); driver.find_element(by=AppiumBy.ID, value=f"{CLOSE_END_LIVE}").click()
        #     print("cant share link 1")
        # except:
        #     pass
        # try: # Close top prodct
        #     time.sleep(1); driver.find_element(by=AppiumBy.XPATH, value=f"{CLOSE_TOP_PRODUCT}").click()
        #     print("cant share link 2")
        # except:
            # pass
        try: driver.find_element(by=AppiumBy.ID, value=f"{BACK_BUTTON}").click()
        except: pass
df = pd.DataFrame(df)
df.to_csv(f'/home/krisna/github/tiktokscraping/data_mei/{CATEGORY}.csv', mode='a', index=False, header=False) # Set up Folder Save File CSV

# # Open Product by "Sold Text"
# def open_product_v2_search_asuspromaxm1(SKIP, CATEGORY, k):
#     actions = TouchAction(driver)
#     element = driver.find_elements(by=AppiumBy.XPATH, value="//com.lynx.tasm.behavior.ui.view.UIView[@content-desc="''terjual")]")
#     el = element[1::2]
#     if k > 0 or SKIP == True: del el[:2]
#     loc = [i.location for i in el]
#     print("list :", loc)

#     df = []
#     for i in loc:
#         try: actions.tap(None, i["x"], i["y"]).perform()
#         except: pass
#         try: close_dialog()
#         except: pass
#         try:
#             time.sleep(1)
#             link = get_link_search_asuspromaxm1()
#             print("found link : ", link)
#             df.append(link)
#         except: pass
#         try:
#             time.sleep(1)
#             driver.swipe(540, 590, 540, 1850, 400) # swipe live product video
#             time.sleep(1)
#             driver.back()
#         except: pass
#     df = pd.DataFrame(df)
#     df.to_csv(f'D:/github/tiktokscraping/csv/{CATEGORY}.csv', mode='a', index=False, header=False)