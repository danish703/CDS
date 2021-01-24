from django import forms

class upload(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()