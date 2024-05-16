from django import forms

class handle(forms.Form):
    handle = forms.CharField(label='Codeforces Handle', max_length=200, required=True)
    min_rating = forms.IntegerField(label='Minimum Difficulty', required=True)
    max_rating = forms.IntegerField(label='Maximum Difficulty', required=True)