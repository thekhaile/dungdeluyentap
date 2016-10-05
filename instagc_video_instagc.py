__author__ = 'khaile'
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from keywords import *
import random
from time import sleep

class InstacgInstaGCVideo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.instagc.com/users/login')
        self.email = 'aWFoa2Vs\n'
        self.password = 'Tm9uY2hhbGFudDEx\n'

    def log_in(self):
        sleep(10)
        # """ click sign in """
        # el = self.driver.find_element(By.XPATH, '//*[contains(text(), "Sign in")]')
        # el.click()
        #
        # sleep(5)
        #
        # """ click connect """
        # el = self.driver.find_element(By.XPATH, '//*[@class ="id_link_text" and contains(text(), "Connect")]')
        # el.click()
        # sleep(5)
        """ enter email """
        el = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        el.send_keys(self.email.decode('base64','strict'))
        sleep(5)
        """ enter password """
        el = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        el.send_keys(self.password.decode('base64','strict'))
        sleep(5)
        """ sign in """
        el = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        el.click()
        sleep(5)


    def navigate_to_recommended(self):
        sleep(5)
        try:
            el = self.driver.find_element(By.XPATH, '//span[contains(text(),"Earn")]')
            el.click()
            sleep(1)
        except:
            pass
        el = self.driver.find_element(By.XPATH, '//*[contains(text(), "Recommended")]')
        el.click()
        sleep(5)
    def navigate_to_video_tab(self):
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//a[contains(text(), "Videos") and @href="/earn/videos"]')
        el.click()
        sleep(5)
    def navigate_to_instagc(self):
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//a[@href="/offers/videos"]')
        el.click()
        sleep(5)

    def launch_content_carousel_window(self):
        sleep(2)
        el = self.driver.find_element(By.XPATH, '//*[text()="Video - Watch Content Carousel"]')
        el.click()
        sleep(5)
    def switch_window(self, originalWindow=None):
        handles = self.driver.window_handles
        if len(handles) > 1:
            for handle in handles:
                if handle != originalWindow:
                    self.driver.switch_to.window(handle)

    def tap_launch_carousel(self):
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//button[text()="Launch Carousel"]')
        el.click()
        sleep(5)

    # def refresh_or_new(self):
    #     condition = random.randint(0,1)
    #     if condition:
    #         try:
    #             el = self.driver.find_element(By.XPATH,'//*[@class="b_topTitle"]')
    #             el.click()
    #             sleep(10)
    #             self.driver.back()
    #         except:
    #             pass
    #     else:
    #         pass

    def test_instagc_video(self):
        self.log_in()
        self.navigate_to_recommended()
        self.navigate_to_video_tab()
        self.navigate_to_instagc()
        firstWindow = self.driver.window_handles[0]
        self.launch_content_carousel_window()
        self.switch_window(firstWindow)
        self.tap_launch_carousel()
        while True:
            sleep(110)
            while len(self.driver.window_handles) > 1:
                self.driver.close()
                self.switch_window(firstWindow)
            self.switch_window()
            sleep(3700)
            self.driver.refresh()
            firstWindow = self.driver.window_handles[0]
            self.launch_content_carousel_window()
            self.switch_window(firstWindow)
            self.tap_launch_carousel()



    def tearDown(self):
        try:
            self.driver.save_screenshot(str(self.id())+'.png')
        except:
            pass
        finally:
            self.driver.close()
