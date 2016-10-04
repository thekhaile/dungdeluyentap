__author__ = 'khaile'
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from keywords import *
import random
from time import sleep

class Instacg(unittest.TestCase):

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


    def navigate_to_videos(self):
        sleep(5)
        try:
            el = self.driver.find_element(By.XPATH, '//span[contains(text(),"Earn")]')
            el.click()
            sleep(1)
        except:
            pass
        el = self.driver.find_element(By.XPATH, '//*[contains(text(), "Watch videos")]')
        el.click()
        sleep(5)

    def play_video(self):
        sleep(5)
        """focus on iframe"""
        self.driver.switch_to_frame(self.driver.find_element(By.TAG_NAME,"iframe"))
        el = self.driver.find_element(By.CSS_SELECTOR, 'div.skin5-play-poster-play-icon.skin5-play-poster-control')
        el.click()

    def check_playlist_ended(self):
        sleep(5)
        self.driver.switch_to_default_content()
        try:
            el = self.driver.find_element(By.XPATH, '//*[@class="issue" and text()="Playlist has ended. Please refresh to start over."]')
            self.navigate_to_videos()
        except:
            pass


    def test1(self):
        self.log_in()
        self.navigate_to_videos()
        while True:
            self.play_video()
            sleep(5400)
            self.check_playlist_ended()


    def tearDown(self):
        try:
            self.driver.save_screenshot('/test1.png')
        except:
            pass
        finally:
            self.driver.close()
