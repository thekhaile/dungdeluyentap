__author__ = 'khaile'
import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from keywords import *
import random
from time import sleep

class BingSearchMobile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'browserName': 'Safari',
                'platformName': 'iOS',
                'platformVersion': '9.2',
                'deviceName': 'iPhone 5s',
                'newCommandTimeout': "7200",
                'launchTimeout': '300000',
                'fullReset': True,
                'noReset': False
            })
        self.driver.get('http://www.bing.com/')
        self.email = 'a2hhaS5sZWhAaG90bWFpbC5jb20=\n'
        self.password = 'Tm9uY2hhbGFudDEx\n'

    def log_in(self):

        sleep(10)
        """click hamburger"""
        el = self.driver.find_element(MobileBy.ID, 'mHamburger')
        el.click()

        sleep(10)
        """ click sign in """
        el = self.driver.find_element(MobileBy.XPATH, '//*[contains(text(), "Sign in") and @id="hb_s"]')
        el.click()
        sleep(5)

        """ enter email """
        el = self.driver.find_element(MobileBy.XPATH, '//input[@type="text"]')
        el.send_keys(self.email.decode('base64','strict'))
        sleep(5)
        """ enter password """
        el = self.driver.find_element(MobileBy.XPATH, '//input[@type="password"]')
        el.send_keys(self.password.decode('base64','strict'))
        sleep(5)
        """ sign in """
        el = self.driver.find_element(MobileBy.XPATH, '//input[@type="submit"]')
        el.click()
        sleep(5)

    def tap(self, element):
        location =  element.location
        size = element.size

        self.driver.switch_to.context('NATIVE_APP')
        webView = self.driver.find_element(MobileBy.CLASS_NAME, 'UIAWebView')
        webLocation = webView.location


        # offsetting location so that the element can be tapped
        location['x'] = location['x'] + size['width']/2
        location['y'] = location['y'] + size['height']/2 + webLocation['y']
        if location['x'] < 0 or location < 0:
            pass
        else:
            self.driver.execute_script('mobile: tap', location)
    def getWebViewLocation(self):
        self.driver.switch_to.context('NATIVE_APP')
        webView = self.driver.find_element(MobileBy.CLASS_NAME, 'UIAWebView')
        webLocation = webView.location
        self.driver.switch_to.context('WEBVIEW_1')
        return webLocation

    def tap_within_webview(self, webLocation, elementLocation):
        self.driver.switch_to.context('NATIVE_APP')
        elementLocation['y'] = webLocation['y'] + elementLocation['y']
        elementLocation['x'] = webLocation['x'] + elementLocation['x']
        self.driver.execute_script('mobile: tap', elementLocation)
        self.driver.switch_to.context('WEBVIEW_1')

    def search(self, keyword):
        sleep(10)
        """ enter keyword """
        el = self.driver.find_element(MobileBy.XPATH, '//input[@type="search"]')
        el.clear()
        el.send_keys(keyword)
        self.tap(el)
        sleep(5)
        try:
            el = self.driver.find_element(MobileBy.XPATH, '//input[@type="submit"]')
            el.click()
        except:
            self.driver.switch_to.context('NATIVE_APP')
            el = self.driver.find_element(MobileBy.XPATH, '//UIAButton[@name="Search"]')
            el.click()
            self.driver.switch_to.context('WEBVIEW_1')
        sleep(5)

    def dismiss_banner(self):
        sleep(10)
        """ enter keyword """
        try:
            el = self.driver.find_element(MobileBy.XPATH, '//img[@class="closeIcon rms_img"]')
            el.click()
            self.driver.refresh()
            sleep(5)

        except:
            pass

    def advance_after_search(self):
        webLocation = self.getWebViewLocation()
        condition = random.randint(0,1)
        if condition:
            try:
                contain = self.driver.find_element(MobileBy.XPATH, '//ol[@role="main" and @aria-label="Search Results"]')
                search = contain.find_element(MobileBy.XPATH, '//li[@class="b_algo"]')
                titleLink = search.find_element(MobileBy.TAG_NAME, 'h2')
                elementLocation = titleLink.location_once_scrolled_into_view
                self.tap_within_webview(webLocation, elementLocation)
                sleep(random.randint(10,20))
                self.driver.back()
                sleep(5)
                if 'https://www.bing.com/search' in self.driver.current_url:
                    pass
                else:
                    self.driver.get('http://www.bing.com/')
            except:
                self.driver.get('http://www.bing.com/')
        else:
            pass

    def search_break(self):
        return random.randint(120, 500)


    def test1(self):
        self.dismiss_banner()
        self.log_in()

        while True:
            keywords = Keywords().get_keywords(option=2)
            for keyword in keywords:
                print keyword
                self.search(keyword)
                self.advance_after_search()
                print self.search_break()
                sleep(self.search_break())
            for i in range(13):
                sleep(random.randint(5400, 6000))
                self.driver.current_url


    def tearDown(self):
        try:
            self.driver.save_screenshot(str(self.id())+'.png')
        except:
            pass
        finally:
            self.driver.quit()
