from django import forms
from .models import Hewan

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Hewan
        fields = ('nama', 'species')