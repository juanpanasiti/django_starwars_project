from django import forms

class MovieForm(forms.Form):
    title = forms.CharField()
    order = forms.IntegerField()
    description = forms.CharField()