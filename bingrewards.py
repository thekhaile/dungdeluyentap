__author__ = 'khaile'
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from keywords import *
import random
from time import sleep

class BingSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.bing.com/')
        self.email = 'a2hhaS5sZWhAaG90bWFpbC5jb20=\n'
        self.password = 'Tm9uY2hhbGFudDEx\n'

    def log_in(self):
        sleep(10)
        """ click sign in """
        el = self.driver.find_element(By.XPATH, '//*[contains(text(), "Sign in")]')
        el.click()

        sleep(5)

        """ click connect """
        el = self.driver.find_element(By.XPATH, '//*[@class ="id_link_text" and contains(text(), "Connect")]')
        el.click()
        sleep(5)
        """ enter email """
        el = self.driver.find_element(By.XPATH, '//input[@type="email"]')
        el.send_keys(self.email.decode('base64','strict'))
        sleep(5)
        """ enter password """
        el = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        el.send_keys(self.password.decode('base64','strict'))
        sleep(5)
        """ sign in """
        el = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        el.click()
        sleep(5)
    def search(self, keyword):
        sleep(10)
        """ enter keyword """
        el = self.driver.find_element(By.XPATH, '//input[@type="search"]')
        el.clear()
        el.send_keys(keyword)
        el.click()
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        el.click()
        sleep(5)

    def advance_after_search(self):
        condition = random.randint(0,1)
        if condition:
            try:
                contain = self.driver.find_element(By.XPATH, '//ol[@role="main" and @aria-label="Search Results"]')
                search = contain.find_element(By.XPATH, '//li[@class="b_algo"]')
                titleLink = search.find_element(By.TAG_NAME, 'h2')
                titleLink.click()
                sleep(10)
                self.driver.back()
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
        self.log_in()
        keywords = Keywords().get_keywords()

        for keyword in keywords:
            print keyword
            self.search(keyword)
            self.advance_after_search()
            sleep(self.search_break())


    def tearDown(self):
        try:
            self.driver.save_screenshot(str(self.id())+'.png')
        except:
            pass
        finally:
            self.driver.close()
