from django import forms
from short_urls.utils import validate_url


class UrlForm(forms.Form):
    url = forms.CharField(validators=[validate_url], label='',
                          widget=forms.TextInput(
                              attrs={
                                  "placeholder": "Введите URL",
                                  "class": "form-control"
                              })
                          )
