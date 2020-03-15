#!/usr/bin/env python
import errno
import os
import random
import string
import time
from email_utils import EmailConnection, Email

import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui_utils import send_keys_delay


class TestSlots(unittest.TestCase):

    @classmethod
    def setUp(self):
        #Create a new Chrome session.
        options = Options()
        options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

        #TODO: SETUP SPANISH - ENGLISH - ... Chrome - Firefox - Safari

        #Create dir for reportes if it does not exist
        try:
            os.makedirs('reportes')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def testTitle(self):
        self.browser.get('https://www.cryptobet.com/')
        self.assertIn('CryptoBet - Crypto & Bitcoin Sports Betting, Casino, and Poker with Automated Instant Payouts',
                      self.browser.title)

    def testSearchEngineCorrect(self):
        """
        tcbet-43
        :return:
        """

    def testSearchEngineIncorrect(self):
        """
        tcbet-44
        :return:
        """

    def testSearchCategoriesSlots(self):
        """
        tcbet-45
        :return:
        """

    def testCategoriesTableGames(self):
        """
        tcbet-46
        :return:
        """

    def testCategoriesVideoPoker(self):
        """
        tcbet-59
        :return:
        """

    def testCategoriesVirtuals(self):
        """
        tcbet-48
        :return:
        """

    def testCategoriesBingoKeno(self):
        """
        tcbet-49
        :return:
        """

    def testProviders(self):
        """
        tcbet-50
        :return:
        """

    def testFavorites(self):
        """
        
        :return:
        """

if __name__ == '__main__':
    unittest.main(verbosity=2)