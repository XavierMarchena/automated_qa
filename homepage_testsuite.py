#!/usr/bin/env python
import errno
import os
import random
import string
import time

import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui_utils import send_keys_delay


class TestHomepage(unittest.TestCase):

    @classmethod
    def setUp(self):
        #Create a new Chrome session.
        options = Options()
        options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

        #TODO: SETUP SPANISH - ENGLISH - ... Chrome - Firefox - Safari
        #Create dir for reports
        try:
            os.makedirs('reportes')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def testTitle(self):
        self.browser.get('https://www.cryptobet.com/')
        self.assertIn('CryptoBet - Crypto & Bitcoin Sports Betting, Casino, and Poker with Automated Instant Payouts',
                      self.browser.title)

    # === tcbet-1 ===
    def testLoginCorrect(self):
        """
        """
        #INPUT DATA
        #TODO: get png name from function
        screenshot_url = 'reportes/testLoginCorrect.png'

        #A valid account
        username = ''
        password = ''

        self.browser.get('https://www.cryptobet.com/')

        # LOGIN BUTTON
        self.login_button_1 = self.browser.find_element_by_xpath('/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/button[2]')
        self.login_button_1.click()

        # LOGIN POPUP
        self.modalLogin = self.browser.find_element_by_id('modalLogin')

        # USERNAME
        self.username_input = self.browser.find_element_by_xpath('/html/body/app-root/app-layout/div/div[1]/div[11]/div/div/div[2]/form/div[1]/input')
        self.username_input.send_keys(username)

        # PASSWORD
        self.password_input = self.browser.find_element_by_xpath('//*[@id="passwordLog"]')
        self.password_input.send_keys(password)

        # LOGIN BUTTON 2
        self.login_button_2 = self.browser.find_element_by_xpath('/html/body/app-root/app-layout/div/div[1]/div[11]/div/div/div[2]/form/div[3]/button')
        self.login_button_2.click()

        #END OF NAVIGATION

        #WAIT AND ASSERT
        try:
            self.user_icon = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/i')))
        finally:
            self.assertTrue(self.user_icon.is_enabled())
            self.browser.save_screenshot(screenshot_url)

    # === tcbet-4-5 ===
    def testLoginIncorrect(self):
        """
        tcbet-5

        """

        #INPUT DATA

        #An invalid account
        username = ''
        password = ''

        self.browser.get('https://www.cryptobet.com/')

        #LOGIN BUTTON
        self.login_button_1 = self.browser.find_element_by_xpath('/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/button[2]')
        self.login_button_1.click()

        #LOGIN POPUP
        self.modalLogin = self.browser.find_element_by_id('modalLogin')

        #USERNAME
        self.username_input = self.browser.find_element_by_xpath('/html/body/app-root/app-layout/div/div[1]/div[11]/div/div/div[2]/form/div[1]/input')
        self.username_input.send_keys(username)

        #PASSWORD
        self.password_input = self.browser.find_element_by_xpath('//*[@id="passwordLog"]')
        self.password_input.send_keys(password)

        #LOGIN BUTTON 2
        self.login_button_2 = self.browser.find_element_by_xpath('/html/body/app-root/app-layout/div/div[1]/div[11]/div/div/div[2]/form/div[3]/button')
        self.login_button_2.click()

        #END OF NAVIGATION

        #WAIT AND ASSERT
        try:
            self.login_button_2 = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-layout/div/div[1]/div[11]/div/div/div[2]/form/div[3]/button')))
        finally:
            self.assertTrue(self.login_button_2.is_enabled())
            self.browser.save_screenshot("reportes/testLoginIncorrect.png")
    # === tcbet-6 ===
    def testLogOut(self):
        """
        tcbet-6

        """
        #INPUT DATA

        #A valid account
        username = ''
        password = ''


        self.browser.get('https://www.cryptobet.com/')

        # LOGIN BUTTON 1
        self.login_button_1 = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/button[2]')
        self.login_button_1.click()

        # LOGIN POPUP
        self.modalLogin = self.browser.find_element_by_id('modalLogin')

        # USERNAME
        self.username_input = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[11]/div/div/div[2]/form/div[1]/input')
        self.username_input.send_keys(username)


        # PASSWORD
        self.password_input = self.browser.find_element_by_xpath('//*[@id="passwordLog"]')
        self.password_input.send_keys(password)

        # LOGIN BUTTON 2
        self.login_button_2 = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[11]/div/div/div[2]/form/div[3]/button')
        self.login_button_2.click()

        # LOGOUT
        try:
            self.logout_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[1]/button')))
        finally:
            self.logout_button.click()

        #WAIT AND ASSERT
        try:
            self.login_button_1 = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/button[2]')))
        finally:
            self.assertTrue(self.login_button_1.is_enabled())
            self.browser.save_screenshot("reportes/testLogOut.png")

    # === tcbet-8 ===
    @unittest.skip("TODO")
    def testPasswordRecoveryEmail(self):
        """
        tcbet-8
        """
        #INPUT DATA

        #VALID MAILINATOR ACCOUNT
        email = ''
        password = ''

    # === tcbet-9 ===
    @unittest.skip("TODO")
    def testPasswordRecoveryIncorrectUsername(self):
        """
        tcbet-9
        :return:
        """

        #INPUT DATA

        #Unregistered username
        username = ''

    #=== tcbet-11 ===
    @unittest.skip("TODO")
    def testSignUpCorrect(self):
        """
        tcbet-11
        """
        #INPUT DATA

        # New email required each signup
        randomUser = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        email = randomUser + '@mailinator.com'
        password = '' #6 char, letter and number

        #START OF NAVIGATION
        self.browser.get('https://www.cryptobet.com/')

        #SIGNUP BUTTON
        self.signup_button_1 = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/button[1]')

        self.signup_button_1.click()


        # Wait to load content
        self.browser.implicitly_wait(2000)

        # Signup popup screen
        self.signup_div = self.browser.find_element_by_id('modalRegister')

        #EMAIL
        self.email_input = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[1]/input')
        send_keys_delay(self.email_input, email)

        #USERNAME
        self.username_input = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[2]/input')
        self.username_input.send_keys(randomUser)

        #PASSWORD
        self.password_input = self.browser.find_element_by_xpath('//*[@id="passwordNew"]')
        self.password_input.send_keys(password)

        #CONFIRM PASSWORD
        self.confirmPassword_input = self.browser.find_element_by_xpath('//*[@id="passwordRe"]')
        self.confirmPassword_input.send_keys(password)

        #AGE CHECKBOX
        self.ageCheck_div = self.browser.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div')
        self.ageCheck_div.click()

        #WAIT FOR ACCEPT BUTTON TO LOAD
        self.browser.implicitly_wait(2000)

        #ACCEPT BUTTON
        self.accept_button = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[8]/button')
        self.accept_button.click()


        #CHANGE TO EMAIL SITE
        self.browser.get('https://www.mailinator.com/v3/index.jsp?zone=public&query='+randomUser+'#/#inboxpane')
        #TODO: xavier@qvotech SEND EMAIL WITH ACCOUNT INFO TO SUPPORT@CBET


        #END OF NAVIGATION

        #SAVE FINAL SCREEN
        self.browser.save_screenshot("reportes/testPasswordRecoveryEmail.png")

    # === tcbet-12
    @unittest.skip("TODO")
    def testSignUpIncorrectEmail(self):
        """
        tcbet-12
        """
        # INPUT DATA
        screenshot_url = 'reportes/testSignUpIncorrectEmail.png'
        # New email/user required each signup
        randomUser = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        email = randomUser + 'wrongformat.com'
        password = ''  # 6 char, letter and number

        # START OF NAVIGATION
        self.browser.get('https://www.cryptobet.com/')

        # SIGNUP BUTTON
        self.signup_button_1 = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/button[1]')

        self.signup_button_1.click()

        # Wait to load content
        self.browser.implicitly_wait(2000)

        # Signup popup screen
        self.signup_div = self.browser.find_element_by_id('modalRegister')

        # EMAIL
        self.email_input = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[1]/input')
        send_keys_delay(self.email_input, email)

        # USERNAME
        self.username_input = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[2]/input')
        self.username_input.send_keys(randomUser)

        # PASSWORD
        self.password_input = self.browser.find_element_by_xpath('//*[@id="passwordNew"]')
        self.password_input.send_keys(password)

        # CONFIRM PASSWORD
        self.confirmPassword_input = self.browser.find_element_by_xpath('//*[@id="passwordRe"]')
        self.confirmPassword_input.send_keys(password)

        # AGE CHECKBOX
        self.ageCheck_div = self.browser.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div')
        self.ageCheck_div.click()

        # WAIT FOR ACCEPT BUTTON TO LOAD
        self.browser.implicitly_wait(2000)

        # ACCEPT BUTTON
        self.accept_button = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[8]/button')
        #self.accept_button.click()

        # Wait to load content
        self.browser.implicitly_wait(4000)

        #TODO: assert
        self.assertFalse(self.accept_button.is_enabled())
        # END OF NAVIGATION

        # SAVE FINAL SCREEN
        self.browser.save_screenshot(screenshot_url)

    # === tcbet-14 ===
    @unittest.skip("TODO")
    def testSignUpIncorrectUser(self):
        """

        :return:
        """
        # INPUT DATA
        screenshot_url = 'reportes/testSignUpIncorrectUser.png'

        # Already signed user
        signedUser = ''
        randomEmail = ''.join(random.choice(string.ascii_uppercase) for _ in range(6)) + '@mailinator.com'
        password = ''  # 6 char, letter and number

        # START OF NAVIGATION
        self.browser.get('https://www.cryptobet.com/')

        # SIGNUP BUTTON
        self.signup_button_1 = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/button[1]')
        self.signup_button_1.click()

        # WAIT
        try:
            # SIGNUP POPUP
            self.signup_div = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, 'modalRegister')))
        finally:
            # EMAIL
            self.email_input = self.browser.find_element_by_xpath(
                '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[1]/input')
            send_keys_delay(self.email_input, randomEmail)

            # USERNAME
            self.username_input = self.browser.find_element_by_xpath(
                '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[2]/input')
            self.username_input.send_keys(signedUser)

            # PASSWORD
            self.password_input = self.browser.find_element_by_xpath('//*[@id="passwordNew"]')
            self.password_input.send_keys(password)

            # CONFIRM PASSWORD
            self.confirmPassword_input = self.browser.find_element_by_xpath('//*[@id="passwordRe"]')
            self.confirmPassword_input.send_keys(password)

            # AGE CHECKBOX
            self.ageCheck_div = self.browser.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div')
            self.ageCheck_div.click()

        # ACCEPT BUTTON
        self.accept_button = self.browser.find_element_by_xpath(
                '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[8]/button')
        self.accept_button.click()

        #END OF NAVIGATION

        #WAIT AND ASSERT
        try:
            self.accept_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[8]/button')))
        finally:
            self.assertTrue(self.accept_button.is_enabled())
            self.browser.save_screenshot(screenshot_url)

        # SAVE FINAL SCREEN
        self.browser.save_screenshot(screenshot_url)

        # ASSERT
        self.assertFalse(self.accept_button.is_enabled())

        # SAVE FINAL SCREEN
        self.browser.save_screenshot(screenshot_url)

    # === tcbet-15 ===
    @unittest.skip("TODO")
    def testSignUpIncorrectPasswordRequirements(self):
        """
        tcbet-15
        :return:
        """
        # INPUT DATA
        # New email required each signup
        randomUser = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        email = randomUser + '@mailinator.com'
        password = ''  # Correct: 6 char, letter and number

        # START OF NAVIGATION
        self.browser.get('https://www.cryptobet.com/')

        # SIGNUP BUTTON
        self.signup_button_1 = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/button[1]')

        self.signup_button_1.click()

        # WAIT
        try:
            # SIGNUP POPUP
            self.signup_div = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, 'modalRegister')))
        finally:
            # EMAIL
            self.email_input = self.browser.find_element_by_xpath(
                '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[1]/input')
            send_keys_delay(self.email_input, email)

            # USERNAME
            self.username_input = self.browser.find_element_by_xpath(
                '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[2]/input')
            self.username_input.send_keys(randomUser)

            # PASSWORD
            self.password_input = self.browser.find_element_by_xpath('//*[@id="passwordNew"]')
            self.password_input.send_keys(password)

            # CONFIRM PASSWORD
            self.confirmPassword_input = self.browser.find_element_by_xpath('//*[@id="passwordRe"]')
            self.confirmPassword_input.send_keys(password)

            # AGE CHECKBOX
            self.ageCheck_div = self.browser.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div')
            self.ageCheck_div.click()

        # ACCEPT BUTTON
        self.accept_button = self.browser.find_element_by_xpath(
                '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[8]/button')

        # ASSERT
        self.assertFalse(self.accept_button.is_enabled())

        # SAVE FINAL SCREEN
        self.browser.save_screenshot("reportes/tcbet-15.png")

    # === tcbet-16 ===
    @unittest.skip("TODO")
    def testSignUpIncorrectPasswordMatch(self):
        """
        tcbet-16
        :return:
        """
        # INPUT DATA

        # New email required each signup
        randomUser = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
        email = randomUser + '@mailinator.com'
        password = ''  # Correct: 6 char, letter and number

        # START OF NAVIGATION
        self.browser.get('https://www.cryptobet.com/')

        # SIGNUP BUTTON
        self.signup_button_1 = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[1]/div/app-navbar/div[2]/div[1]/mdb-navbar/nav/div[2]/links/ul/li/div[3]/button[1]')
        self.signup_button_1.click()

        #WAIT
        try:
            # SIGNUP POPUP
            self.signup_div = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, 'modalRegister')))
        finally:
            # EMAIL
            self.email_input = self.browser.find_element_by_xpath(
                '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[1]/input')
            send_keys_delay(self.email_input, email)

            # USERNAME
            self.username_input = self.browser.find_element_by_xpath(
                '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[2]/input')
            self.username_input.send_keys(randomUser)

            # PASSWORD
            self.password_input = self.browser.find_element_by_xpath('//*[@id="passwordNew"]')
            self.password_input.send_keys(password)

            # CONFIRM PASSWORD
            self.confirmPassword_input = self.browser.find_element_by_xpath('//*[@id="passwordRe"]')
            self.confirmPassword_input.send_keys(password + 'IncorrectPasswordMatch')

            # AGE CHECKBOX
            self.ageCheck_div = self.browser.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div')
            self.ageCheck_div.click()


        #END OF NAVIGATION

        # ACCEPT BUTTON
        self.accept_button = self.browser.find_element_by_xpath(
            '/html/body/app-root/app-layout/div/div[1]/div[10]/div/div/div[2]/form/div[8]/button')

        # ASSERT
        self.assertFalse(self.accept_button.is_enabled())
        # SAVE FINAL SCREEN
        self.browser.save_screenshot("reportes/tcbet-16.png")

    # === tcbet-17 ===
    @unittest.skip("TODO")
    def testSignUpIncorrectAgeCheckbox(self):
        """
        tcbet-17
        :return:
        """

    # === tcbet-18 ===
    @unittest.skip("TODO")
    def testContactUsLogged(self):
        """
        tcbet-18
        :return:
        """

    # === tcbet-19 ===
    @unittest.skip("TODO")
    def testContactUsNotLogged(self):
        """
        tcbet-19
        :return:
        """
    # === tcbet-20 ===
    @unittest.skip("TODO")
    def testInformationLinks(self):
        """
        tcbet-20
        :return:
        """

    # === tcbet-21 ===
    @unittest.skip("TODO")
    def testSportsbookLinks(self):
        """
        tcbet-21
        :return:
        """

    # === tcbet-22 ===
    @unittest.skip("TODO")
    def testCasinoLink(self):
        """
        tcbet-22
        :return:
        """

    # === tcbet-23 ===
    @unittest.skip("TODO")
    def testNetworkLinks(self):
        """
        tcbet-23
        :return:
        """


    # === tcbet-24 ===
    @unittest.skip("TODO")
    def testSocialMediaLinks(self):
        """
        tcbet-24
        :return:
        """

    # === tcbet-25 ===
    @unittest.skip("TODO")
    def testFooterIcons(self):
        """
        tcbet-25
        :return:
        """
    # === tcbet-33 ===
    @unittest.skip("TODO")
    def testFavoritesAddGame(self):
        """
        tcbet-33
        :return:
        """

    # === tcbet-34 ===
    @unittest.skip("TODO")
    def testFavoritesRemoveGame(self):
        """
        tcbet-34
        :return:
        """

    # === tcbet-35 ===
    @unittest.skip("TODO")
    def testCasino(self):
        """
        tcbet-35
        :return:
        """

    # === tcbet-36 ===
    @unittest.skip("TODO")
    def testSports(self):
        """
        tcbet-36
        :return:
        """

    # === tcbet-38 ===
    @unittest.skip("TODO")
    def testLiveCasinoEvolution(self):
        """
        tcbet-38
        :return:
        """
    # === tcbet-39 ===
    @unittest.skip("TODO")
    def testLiveCasinoVivoGMG(self):
        """
        tcbet-39
        :return:
        """

    # === tcbet-39 ===
    @unittest.skip("TODO")
    def testLiveCasinoAsiaGMG(self):
        """
        tcbet-39
        :return:
        """
    # === tcbet-40 ===
    @unittest.skip("TODO")
    def testCommunity(self):
        """
        tcbet-40
        :return:
        """

    @classmethod
    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
