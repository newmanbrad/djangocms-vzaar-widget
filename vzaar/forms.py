from django import forms
from cms.plugins.vzaar.models import Vzaar

class VzaarForm(forms.ModelForm):
    
    class Meta:
        model = Vzaar
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')