from appium import webdriver
from common import *
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
import os
from appium.webdriver.common.touch_action import TouchAction


def main():
    email = 'a2hhaS5sZWh1eW5oQGdtYWlsLmNvbQ==\n'
    password = 'bm9uY2hhbGFudDEx\n'
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': '../../../TestApps/swagbucks.apk',
            'platformName': 'Android',
            'deviceName': '6.0',
            'newCommandTimeout': "7200",
            'fullReset': True,
            'noReset': False
        })
    driver.implicitly_wait(5)
    app = Device(driver)
    UIType = Type(driver)
    action = TouchAction(driver)

    # if app.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/welcome_screen_viewPager'):
    #     pass
    sleep(5)

    for i in range(3):
        app.swipe_left()
        sleep(2)

    ###Sign in
    #Navigate to Login
    el = app.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/register_screen_ButtunLogin')
    UIType.Button(el).tap()

    #Enter Email
    el = app.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/login_screen_editTextEmail')
    UIType.TextField(el).enter_text(email.decode('base64', 'strict'))

    #Enter Password
    el = app.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/login_screen_editTextPassword')
    UIType.TextField(el).enter_text(password.decode('base64', 'strict'))

    #Tap login
    el = app.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/login_screen_ButonLogin')
    UIType.Button(el).tap()

    #Tap menu icon
    el = app.find_element(MobileBy.ID, 'Open navigation drawer')
    UIType.Button(el).tap()

    #get Listview
    listView = app.find_element(MobileBy.CLASS_NAME, 'android.widget.ListView')
    items = listView.find_elements(MobileBy.CLASS_NAME, 'android.widget.RelativeLayout')

    for item in items[5:15]:
        UIType.Button(item).tap()
        for i in range(40):
            View = app.find_element(MobileBy.CLASS_NAME, 'android.support.v7.widget.RecyclerView')
            cells = View.find_elements(MobileBy.CLASS_NAME, 'android.widget.FrameLayout')
            for cell in cells:
                try:
                    el = cell.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/row_video_red_heart_imageview')
                    continue
                except:
                    coordinates = cell.location
                    size = cell.size
                    coordinates['x'] = coordinates['x']+ size['width']/2
                    coordinates['y'] = coordinates['y']+ size['height']/2
                    action.long_press(x=coordinates['x'], y=coordinates['y']).perform()
                    sleep(2)
                    #Add to favorites
                    if app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Add to Favorites")'):
                        el = app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Add to Favorites")')
                        UIType.Button(el).tap()
                    else:
                        el = app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Cancel")')
                        UIType.Button(el).tap()
            for i in range(1):
                app.swipe_up()
            View = app.find_element(MobileBy.CLASS_NAME, 'android.support.v7.widget.RecyclerView')
            cells = View.find_elements(MobileBy.CLASS_NAME, 'android.widget.FrameLayout')

            #Tap menu icon
        el = app.find_element(MobileBy.ID, 'Open navigation drawer')
        UIType.Button(el).tap()
        items = listView.find_elements(MobileBy.CLASS_NAME, 'android.widget.RelativeLayout')

    #Tap menu icon
    el = app.find_element(MobileBy.ID, 'Open navigation drawer')
    UIType.Button(el).tap()

    #Tap Favorites
    listView = app.find_element(MobileBy.CLASS_NAME, 'android.widget.ListView')
    items = listView.find_elements(MobileBy.CLASS_NAME, 'android.widget.RelativeLayout')
    item = items[3]
    UIType.Button(item).tap()

    View = app.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/video_recycler_view')
    cell = View.find_element(MobileBy.CLASS_NAME, 'android.widget.FrameLayout')
    UIType.Button(cell).tap()
    while True:
        continue
main()