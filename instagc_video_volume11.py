__author__ = 'khaile'
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from keywords import *
import random
from time import sleep

class InstacgVolume11Video(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
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
    def navigate_to_volume11(self):
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//a[@href="/earn/volume11"]')
        el.click()
        sleep(5)

    def launch_volume11_window(self):
        sleep(2)
        el = self.driver.find_element(By.XPATH, '//a[@class="button action" and text()= "Launch Volume11 in a new window"]')
        el.click()
        sleep(5)
    def switch_window(self, originalWindow=None):
        handles = self.driver.window_handles
        if len(handles) > 1:
            for handle in handles:
                if handle != originalWindow:
                    self.driver.switch_to.window(handle)
        else:
            self.driver.switch_to.window(handles[0])
    def tap_next(self):
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//*[@class="btn" and @id="next_btn"]')
        el.click()
        sleep(5)

    def tap_play(self):
        sleep(15)
        check = False
        while not check:
            try:
                self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME,"iframe"))
                try:
                    el = self.driver.find_element(By.TAG_NAME,"iframe")
                    if el.get_attribute('title') == 'YouTube video player':
                        break
                except:
                    pass
            except:
                check = True

        self.driver.switch_to.frame('player')
        el = self.driver.find_element(By.CSS_SELECTOR, 'button.ytp-large-play-button.ytp-button')
        el.click()
        sleep(5)

    def refresh_or_new(self):
        condition = random.randint(0,1)
        if condition:
            try:
                el = self.driver.find_element(By.XPATH,'//*[@class="b_topTitle"]')
                el.click()
                sleep(10)
                self.driver.back()
            except:
                pass
        else:
            pass

    def test_volume11_video(self):
        self.log_in()
        self.navigate_to_recommended()
        self.navigate_to_video_tab()
        self.navigate_to_volume11()
        firstWindow = self.driver.window_handles[0]
        self.launch_volume11_window()
        self.switch_window(firstWindow)
        while True:
            try:
                self.tap_play()
            except:
                pass
            sleep(600)
            self.driver.switch_to.default_content()
            condition = random.randint(0,1)
            if condition:
                try:
                    self.tap_next()
                except:
                    self.driver.refresh()
            else:
                self.driver.close()
                self.switch_window()
                firstWindow = self.driver.window_handles[0]
                self.launch_volume11_window()
                self.switch_window(firstWindow)




    def tearDown(self):
        try:
            self.driver.save_screenshot(str(self.id())+'.png')
        except:
            pass
        finally:
            self.driver.close()
