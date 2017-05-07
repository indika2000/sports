from django.shortcuts import render, redirect
from fixtures.forms import TeamIdForm
from lib.sampler import get_team_fixture_codes
import json

def locahost_redirect(request):
    """ redirect any traffic to localhost root to the fixtures page"""
    return redirect('/fixtures')

def fixtures_page(request):
    if request.method == 'POST':
        form = TeamIdForm(request.POST)

        if form.is_valid():
            #return HttpResponse('<html><body><h1>Hello</h1></body></html>')
            return redirect('/fixtures/%s' % request.POST['team_id'])
    else:
        form = TeamIdForm()


    return render(request, 'fixtures.html', {'form': form})

def team_fixture(request, team_id):

    contents = get_team_fixture_codes(team_id)

    return render(request, 'fixtures_results.html', {'fixtures': contents})

