from django import forms
from .validator import validate_url

class url_form(forms.Form):
	url = forms.CharField(label="Enter URL:",validators=[validate_url])