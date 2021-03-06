__author__ = 'khaile'
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from keywords import *
import random
from time import sleep
from common import *

class InstacgVideo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.instagc.com/users/login')
        self.email = 'aWFoa2Vs\n'
        self.password = 'Tm9uY2hhbGFudDEx\n'
        self.app = Device(self.driver)

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
        # try:
        #     el = self.driver.find_element(By.XPATH, '//span[contains(text(),"Earn")]')
        #     el.click()
        #     sleep(1)
        # except:
        #     pass
        # el = self.driver.find_element(By.XPATH, '//*[contains(text(), "Watch videos")]')
        # el.click()
        self.driver.get('https://www.instagc.com/watch/')
        sleep(5)

    def choose_playlist(self):
        n = random.randint(0,2)
        els = self.driver.find_elements(By.CLASS_NAME, 'playlist-show')
        el = els[n]
        el.click()
        sleep(3)
    def play_video(self):
        sleep(5)
        try:
            """focus on iframe"""
            self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME,"iframe"))
            el = self.driver.find_element(By.CSS_SELECTOR, 'div.skin5-poster-play-icon.poster-control')
        except:
            try:
                el = self.driver.find_element(By.CSS_SELECTOR, 'div.skin5-play-poster-play-icon.skin5-play-poster-control')

            except:
                self.driver.refresh()
                sleep(5)
                self.check_playlist_ended()
                try:
                    self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME,"iframe"))
                    el = self.driver.find_element(By.CSS_SELECTOR, 'div.skin5-poster-play-icon.poster-control')
                except:
                    el = self.driver.find_element(By.CSS_SELECTOR, 'div.skin5-play-poster-play-icon.skin5-play-poster-control')
        el.click()


    def check_playlist_ended(self):
        sleep(5)
        try:
            before_count = self.app.find_element(By.ID,'watch-progress').text
            print before_count
            sleep(600)
            after_count = self.app.find_element(By.ID,'watch-progress').text
            print after_count
            if before_count == after_count:
                print 'Video watching is not being counted'
                print 'navigate to watch'
                self.driver.get('https://www.instagc.com/watch/')
                sleep(5)
                print 'Open playlist'
                self.choose_playlist()
                self.driver.switch_to.default_content()

        # try:
        #     self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME,"iframe"))
        #     if self.app.find_element(By.CLASS_NAME, 'video-duration'):
        #         for i in range(2):
        #             duration = self.app.find_element(By.CLASS_NAME, 'video-duration').text
        #             progress = self.app.find_element(By.CLASS_NAME, 'video-progress-time').text
        #             sleep(2)
        #         if duration == progress:
        #             print 'Spinning'
        #             print 'navigate to watch'
        #             self.driver.get('https://www.instagc.com/watch/')
        #             sleep(5)
        #             print 'Open playlist'
        #             self.choose_playlist()
        #             self.driver.switch_to.default_content()
        except:
            try:
                self.driver.switch_to.default_content()
                el = self.driver.find_element(By.XPATH, '//*[@class="issue" and text()="Playlist has ended. Please refresh to start over."]')
                print 'playlist ended'
                sleep(3)
                self.driver.get('https://www.instagc.com/watch/')
                sleep(5)
                self.choose_playlist()
                self.driver.switch_to.default_content()
            except:
                try:
                    self.driver.switch_to.default_content()
                    el = self.driver.find_element(By.XPATH, '//*[contains(text(), "inventory has temporarily ran out"]')
                    print 'Out of inventory'
                    sleep(3600)
                    self.driver.get('https://www.instagc.com/watch/')
                    sleep(5)
                    self.choose_playlist()
                    self.driver.switch_to.default_content()
                except:
                    pass



    def test_video(self):
        self.log_in()
        self.navigate_to_videos()
        self.choose_playlist()
        while True:
            self.check_playlist_ended()
            # self.play_video()
            # sleep(600)
            # self.check_playlist_ended()


    def tearDown(self):
        try:
            self.driver.save_screenshot(str(self.id())+'.png')
        except:
            pass
        finally:
            self.driver.close()
