from django import forms
from .validator import validate_url

class url_form(forms.Form):
	url = forms.CharField(
			label="",
			validators=[validate_url],
			widget=forms.TextInput(
				attrs = {
					"placeholder":"URL",
					"class":"form-control"
				}
			)
		)