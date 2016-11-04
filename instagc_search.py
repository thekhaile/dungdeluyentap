__author__ = 'khaile'
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from keywords import *
import random
from time import sleep

class InstacgSearch(unittest.TestCase):

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


    def navigate_to_search(self):
        sleep(5)
        self.driver.get('https://www.instagc.com/search/')
        sleep(5)

    def search(self, keyword):
        sleep(10)
        """ enter keyword """
        el = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        el.clear()
        el.send_keys(keyword)
        el.click()
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
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
    def advance_after_search(self):
        condition = random.randint(0,1)
        if condition:
            try:
                self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME,"iframe"))
                container = self.driver.find_element(By.CSS_SELECTOR, 'ul.ypaAdUnit')
                search = container.find_element(By.CSS_SELECTOR, 'li.ypaAdElement.ypaAdSpacing')
                titleLink = search.find_element(By.CSS_SELECTOR, 'span.ypaAdTitleInner')
                firstWindow = self.driver.window_handles[0]
                titleLink.click()
                sleep(random.randint(5,15))
                if len(self.driver.window_handles) > 1:
                    self.switch_window(firstWindow)
                    self.driver.close()
                    self.switch_window()
                else:
                    self.driver.get('https://www.instagc.com/search/')
            except:
                self.driver.get('https://www.instagc.com/search/')
        else:
            pass

    def search_break(self):
        return random.randint(110, 300)

    def test_search(self):
        self.log_in()
        self.navigate_to_search()
        keywords = Keywords().get_keywords()
        while True:
            for keyword in keywords:
                try:
                    print keyword
                    self.search(keyword)
                    # self.advance_after_search()
                    print self.search_break()
                    sleep(self.search_break())
                except:
                    self.navigate_to_search()
            keywords = Keywords().get_keywords()


    def tearDown(self):
        try:
            self.driver.save_screenshot(str(self.id())+'.png')
        except:
            pass
        finally:
            self.driver.close()
