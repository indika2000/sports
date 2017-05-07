""" Functional test class for basic url checking and base functional tests"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time
import json

class OpenFixturesLandingPage(LiveServerTestCase):
    """ Opening Test for reaching the Idople Landing PAGE"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()

    def test_open_landingpage_check_title(self):
        self.browser.get(self.live_server_url + '/fixtures')
        self.assertIn('Team Fixtures - Enter an ID, find the fixtures', self.browser.title)

    def test_root_url_redirects_to_fixtures(self):
        self.browser.get(self.live_server_url)
        self.browser.implicitly_wait(2)
        self.assertIn('Team Fixtures - Enter an ID, find the fixtures', self.browser.title)

    def test_enter_wrong_url(self):
        self.browser.get(self.live_server_url + '/fdgdfgjfdgjnfgkjnfdkgnfdkjng')
        self.browser.implicitly_wait(2)

        #Incorrect URL should redirect to the fixtures page
        self.assertIn(self.live_server_url + '/fixtures', self.browser.current_url)


class EnterTeamIds(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

        #The user navigates to the url
        self.browser.get(self.live_server_url + '/fixtures')

    def tearDown(self):
        self.browser.quit()

    def test_entering_team_id_413(self):
        #They enter the team id 413 in the txt box
        inputTeamId = self.browser.find_element_by_id('id_team_id')
        inputTeamId.send_keys('413')
        inputTeamId.send_keys(Keys.ENTER)

        #sleep to prevent the next assert from running before the results return.
        time.sleep(3)

        #Check we've redirected to the correct team url & capture the return results
        self.assertIn(self.live_server_url + '/fixtures/413/', self.browser.current_url)

        #Check that results are coming back
        table = self.browser.find_element_by_id('id_team_fixtures')
        rows = table.find_elements_by_tag_name('tr')
        r = [row.text for row in rows]

        self.assertIn('item', r[0])

    def test_team_id_nonnumerical(self):
        #The user navigates to the url
        self.browser.get(self.live_server_url + '/fixtures')

        #The user enters a nonsensical id i.e. a word
        inputTeamId = self.browser.find_element_by_id('id_team_id')
        inputTeamId.send_keys('Arsenal Rule!') #Don't let the fact I'm an Arsenal fan put you off. :)
        inputTeamId.send_keys(Keys.ENTER)

        #The webapp should take this string and redirect the user to input again
        #A longer implementation would return an error page, or better yet have javascript
        #to prevent submission
        time.sleep(3)
        self.assertIn(self.live_server_url + '/fixtures', self.browser.current_url)
