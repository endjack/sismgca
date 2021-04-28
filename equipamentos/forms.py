from django import forms
from .models import *

class Par2000TForm(forms.ModelForm):
    class Meta:
        model = Par2000T
        fields = ['situacao']

class ConsolesForm(forms.ModelForm):
    class Meta:
        model = Consoles
        fields = ['situacao']

class RadiosForm(forms.ModelForm):
    class Meta:
        model = Radios
        fields = ['situacao']

class CentralAudioForm(forms.ModelForm):
    class Meta:
        model = CentralAudio
        fields = ['situacao']

class DiversosForm(forms.ModelForm):
    class Meta:
        model = Diversos
        fields = ['situacao']

class EmsForm(forms.ModelForm):
    class Meta:
        model = Ems
        fields = ['situacao']

class TelefoniaForm(forms.ModelForm):
    class Meta:
        model = Telefonia
        fields = ['situacao']



