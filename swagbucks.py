__author__ = 'khaile'
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from keywords import *
import random
from time import sleep

class SwagSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.swagbucks.com/p/login')
        self.email = 'a2hhaS5sZWh1eW5oQGdtYWlsLmNvbQ==\n'
        self.password = 'bm9uY2hhbGFudDEx\n'

    def log_in(self):
        sleep(10)
        # """ click sign in """
        # el = self.driver.find_element(By.XPATH, '//*[@href="http://www.swagbucks.com/p/login"]')
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
        el = self.driver.find_element(By.XPATH, '//*[@id="loginBtn"]')
        el.click()
        sleep(5)

    def is_swagButton_modal_present(self):
        sleep(5)
        try:
            el = self.driver.find_element(By.XPATH, '//*[@id="swagButtonModal"]')
            return True
        except:
            return False
    def dismiss_swagButton_modal(self):
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//button[@id="swagButtonModalExit"]')
        el.click()
        sleep(5)

    def navigate_to_search(self):
        sleep(5)
        try:
            el = self.driver.find_element(By.XPATH, '//*[@class="sbCta" and @id="sbMainNavToggle"]')
            el.click()
            sleep(5)
        except:
            pass
        el = self.driver.find_element(By.XPATH, '//*[@class="sbMainNavSectionListCta" and text()="Search"]')
        el.click()
        sleep(5)

    def navigate_to_watch(self):
        sleep(5)
        try:
            el = self.driver.find_element(By.XPATH, '//*[@class="sbCta" and @id="sbMainNavToggle"]')
            el.click()
            sleep(5)
        except:
            pass
        el = self.driver.find_element(By.XPATH, '//*[@class="sbMainNavSectionListCta" and text()="Watch"]')
        el.click()
        sleep(5)

    def navigate_back_to_watch_home(self):
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//*[@class="sbMainNavSectionListCta" and text()="Watch Home"]')
        el.click()
        sleep(5)

    def navigate_to_editor_picks(self):
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//*[@href="/watch/playlists/111/editors-pick" and text()="View All"]')
        el.location_once_scrolled_into_view
        el.click()
        sleep(10)

    def get_Playlist_cards(self):
        el = self.driver.find_element(By.ID, 'cardDeck')
        cards = el.find_elements_by_css_selector('section')
        return cards

    def get_playlist_duration(self, card):
        timeContainer = card.find_element(By.CLASS_NAME, 'sbTrayListItemTimeContainer')
        time = timeContainer.find_element_by_css_selector('var').text
        return time

    def get_playlist_video_count(self, card):
        container = card.find_element(By.CLASS_NAME, 'sbTrayListItemSbType')
        count = container.find_element_by_css_selector('var').text
        return count

    def start_playlist(self, card):
        card.location_once_scrolled_into_view
        el = card.find_element(By.CLASS_NAME, 'sbTrayListItemHeaderImgContainer')
        el.click()
        sleep(5)

    def search(self, keyword):
        sleep(10)
        """ enter keyword """
        el = self.driver.find_element(By.XPATH, '//input[@type="text" and @id="sawInput"]')
        el.clear()
        el.send_keys(keyword)
        el.click()
        sleep(5)
        el = self.driver.find_element(By.XPATH, '//button[@id="sawSubmit"]')
        el.click()
        sleep(5)


    def search_break(self):
        return random.randint(120, 500)


    def testSearch(self):
        self.log_in()
        keywords = Keywords().get_keywords()
        if self.is_swagButton_modal_present():
            self.dismiss_swagButton_modal()
        self.navigate_to_search()
        for keyword in keywords[:20]:
            print keyword
            self.search(keyword)
            sleep(self.search_break())
            self.driver.back()

    def testVideos_EditorPicks(self):
        self.log_in()
        if self.is_swagButton_modal_present():
            self.dismiss_swagButton_modal()
        self.navigate_to_watch()
        self.navigate_to_editor_picks()
        cards = self.get_Playlist_cards()
        length = len(cards)
        for i in range(1, length, 1):
            card = cards[i]
            playlist_duration = eval(self.get_playlist_duration(card))*60
            video_count = eval(self.get_playlist_video_count(card))
            commercial_duration = 20*video_count
            total_duration = playlist_duration+commercial_duration+60
            print total_duration
            self.start_playlist(card)
            sleep(total_duration)
            self.navigate_back_to_watch_home()
            self.navigate_to_editor_picks()
            cards = self.get_Playlist_cards()


    def tearDown(self):
        try:
            self.driver.save_screenshot(str(self.id())+'.png')
        except:
            pass
        finally:
            self.driver.close()

