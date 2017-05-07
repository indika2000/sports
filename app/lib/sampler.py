from bs4 import BeautifulSoup as bs
import requests
import json


def get_team_fixture_codes(team_id):
    """ Scrape the JSON details from the team fixtures page
        - A success is if the contents dictionary contains an 'item' key
    """

    try:
        url = 'http://a.365dm.com/api/score-centre/v1/football/team/fixtures/%s' % team_id
        requesturl = requests.get(url)
        soup = bs(requesturl.text, 'html.parser')
        contents = json.loads(str(soup))
    except:
        return {'error': 'Team Fixture Error'}

    if 'items' in contents:
        return get_team_fixtures(contents)
    else:
        return {'Team Id Error': 'Team id Error'}


def get_team_fixtures(team_id_codes):

    if 'items' in team_id_codes:
        codelist = team_id_codes['items']
        fixtures = list()

        for keys in codelist:
            try:
                url = 'http://d.365dm.com/api/score-centre/v1/football/fixture/%s' % keys
                requesturl = requests.get(url)
                soup = bs(requesturl.text, 'html.parser')
                fixtures.append(json.loads(str(soup)))
            except:
                return {'Fixture Error': 'Team fixture Error'}

        return fixtures
    else:
        return {'Code Id Error': 'Team Id Codes incorrect'}