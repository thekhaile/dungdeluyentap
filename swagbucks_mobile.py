from appium import webdriver
from common import *
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
import os
from appium.webdriver.common.touch_action import TouchAction


def main():
    try:
        email = 'a2hhaS5sZWh1eW5oQGdtYWlsLmNvbQ==\n'
        password = 'bm9uY2hhbGFudDEx\n'
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': '../../../TestApps/swagbucks.apk',
                'platformName': 'Android',
                'deviceName': '6.0',
                'newCommandTimeout': "7200",
                'fullReset': False,
                'noReset': True
            })
        driver.implicitly_wait(10)
        app = Device(driver)
        UIType = Type(driver)
        action = TouchAction(driver)

        # if app.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/welcome_screen_viewPager'):
        #     pass

        sleep(5)

        if not app.find_element(MobileBy.ID, 'Open navigation drawer'):
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
            sleep(2)

        #Tap menu icon
        el = app.find_element(MobileBy.ID, 'Open navigation drawer')
        UIType.Button(el).tap()

        # #get Listview
        # list = ['Featured Videos', 'Recipes', 'Entertainment', 'Fashion', 'Health', 'Home and Garden', 'Music',
        #         'News', 'Travel', 'Celebrity']
        #
        #
        # for item in range(0,5):
        #     UIType.Button(app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("%s")' %list[item])).tap()
        #     for i in range(50):
        #         View = app.find_element(MobileBy.CLASS_NAME, 'android.support.v7.widget.RecyclerView')
        #         # cells = View.find_elements(MobileBy.CLASS_NAME, 'android.widget.FrameLayout')
        #         images = View.find_elements(MobileBy.ID, 'com.swagbuckstvmobile.views:id/row_video_thumb_imageview')
        #         hearts = app.find_elements(MobileBy.ID, 'com.swagbuckstvmobile.views:id/row_video_red_heart_imageview')
        #         if (len(images)-len(hearts))>=2:
        #             for image in images:
        #                 try:
        #                     el = image.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/row_video_red_heart_imageview')
        #                 except:
        #                     el = None
        #                 if not el:
        #                     coordinates = image.location
        #                     size = image.size
        #                     coordinates['x'] = coordinates['x']+ size['width']/2
        #                     coordinates['y'] = coordinates['y']+ size['height']/2
        #                     action.long_press(x=coordinates['x'], y=coordinates['y']).perform()
        #                     sleep(2)
        #                     #Add to favorites
        #                     if app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Add to Favorites")'):
        #                         el = app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Add to Favorites")')
        #                         UIType.Button(el).tap()
        #                     else:
        #                         el = app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Cancel")')
        #                         UIType.Button(el).tap()
        #         for i in range(1):
        #             try:
        #                 app.swipe_up()
        #                 sleep(1)
        #             except:
        #                 pass
        #
        #     #Tap menu icon
        #     el = app.find_element(MobileBy.ID, 'Open navigation drawer')
        #     UIType.Button(el).tap()
        #
        # sleep(2)
        # app.swipe_up()
        #
        # for item in range(5,10):
        #     UIType.Button(app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("%s")' %list[item])).tap()
        #     for i in range(50):
        #         View = app.find_element(MobileBy.CLASS_NAME, 'android.support.v7.widget.RecyclerView')
        #         # cells = View.find_elements(MobileBy.CLASS_NAME, 'android.widget.FrameLayout')
        #         images = View.find_elements(MobileBy.ID, 'com.swagbuckstvmobile.views:id/row_video_thumb_imageview')
        #         hearts = app.find_elements(MobileBy.ID, 'com.swagbuckstvmobile.views:id/row_video_red_heart_imageview')
        #         if (len(images)-len(hearts))>=2:
        #             for image in images:
        #                 try:
        #                     el = image.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/row_video_red_heart_imageview')
        #                 except:
        #                     el = None
        #                 if not el:
        #                     coordinates = image.location
        #                     size = image.size
        #                     coordinates['x'] = coordinates['x']+ size['width']/2
        #                     coordinates['y'] = coordinates['y']+ size['height']/2
        #                     action.long_press(x=coordinates['x'], y=coordinates['y']).perform()
        #                     sleep(2)
        #                     #Add to favorites
        #                     if app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Add to Favorites")'):
        #                         el = app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Add to Favorites")')
        #                         UIType.Button(el).tap()
        #                     else:
        #                         el = app.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Cancel")')
        #                         UIType.Button(el).tap()
        #         for i in range(1):
        #             try:
        #                 app.swipe_up()
        #                 sleep(1)
        #             except:
        #                 pass
        #
        # #Tap menu icon
        # el = app.find_element(MobileBy.ID, 'Open navigation drawer')
        # UIType.Button(el).tap()
        #
        # #Tap swipe down
        # sleep(2)
        # app.swipe_down()

        #Tap Favorites
        listView = app.find_element(MobileBy.CLASS_NAME, 'android.widget.ListView')
        items = listView.find_elements(MobileBy.CLASS_NAME, 'android.widget.RelativeLayout')
        item = items[3]
        UIType.Button(item).tap()

        View = app.find_element(MobileBy.ID, 'com.swagbuckstvmobile.views:id/video_recycler_view')
        cell = View.find_element(MobileBy.CLASS_NAME, 'android.widget.FrameLayout')
        UIType.Button(cell).tap()
        while True:
            sleep(3600)
            print 'tap on screen'
            app.tap_on_screen()
            continue
    except:
        app.save_screenshot('swagbucks_mobile.png')
main()