from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from fixtures.views import fixtures_page, team_fixture
from lib.sampler import get_team_fixture_codes, get_team_fixtures
import json
from bs4 import BeautifulSoup as bs
import requests

class FixtureTest(TestCase):

    def test_root_fixtureurl_resolves_to_page_view(self):
        found = resolve('/fixtures')
        self.assertEqual(found.func, fixtures_page)

    def test_root_page_returns_correct_html(self):
        request = HttpRequest()
        response = fixtures_page(request)
        html = response.content.decode('utf-8')

        self.assertIn('<title>Team Fixtures - Enter an ID, find the fixtures</title>', html)

    def test_fixtures_team_id_413_url_resolve(self):
        found = resolve('/fixtures/%d/' % 413)
        self.assertEqual(found.func, team_fixture)


class ScrapeTests(TestCase):

    def test_fixture_code_returns_with_team_id_413_details(self):
        contents = get_team_fixture_codes('413')
        self.assertIn('item', contents[0])


    def test_fixture_code_returns_with_appropriate_error(self):
        contents = get_team_fixture_codes('41xaa3')
        self.assertIn('Team Id Error', contents)

    def test_fixture_scrape_code_post_a_successful_team_id_413(self):
        team_id = 413
        url = 'http://a.365dm.com/api/score-centre/v1/football/team/fixtures/%s' % team_id
        requesturl = requests.get(url)
        soup = bs(requesturl.text, 'html.parser')
        contents = json.loads(str(soup))

        result = get_team_fixtures(contents)

        self.assertIn('item', result[0])


    def test_fixture_scrape_code_post_an_appropriate_error_with_bad_team_id(self):
        team_id = '41sfdsf3'
        url = 'http://a.365dm.com/api/score-centre/v1/football/team/fixtures/%s' % team_id
        requesturl = requests.get(url)
        soup = bs(requesturl.text, 'html.parser')
        contents = json.loads(str(soup))

        result = get_team_fixtures(contents)

        self.assertIn('Code Id Error', result)

    def test_bad_item_codes_returned_from_get_team_fixture_codes(self):
        mockTeamFixtureIds = {'items': ['abc']}
        result = get_team_fixtures(mockTeamFixtureIds)

        self.assertIn('error', result[0])
