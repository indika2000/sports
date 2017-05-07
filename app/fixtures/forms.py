from django import forms

class TeamIdForm(forms.Form):
    team_id = forms.CharField(label="Enter Team Id", max_length=100)