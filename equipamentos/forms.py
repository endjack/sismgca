from django import forms
from .models import *

class Par2000TForm(forms.ModelForm):
    class Meta:
        model = Par2000T
        fields = ['situacao', 'descricao']

class ConsolesForm(forms.ModelForm):
    class Meta:
        model = Consoles
        fields = ['situacao', 'descricao']

class RadiosForm(forms.ModelForm):
    class Meta:
        model = Radios
        fields = ['situacao', 'descricao']

class CentralAudioForm(forms.ModelForm):
    class Meta:
        model = CentralAudio
        fields = ['situacao', 'descricao']

class DiversosForm(forms.ModelForm):
    class Meta:
        model = Diversos
        fields = ['situacao', 'descricao']

class EmsForm(forms.ModelForm):
    class Meta:
        model = Ems
        fields = ['situacao', 'descricao']

class TelefoniaForm(forms.ModelForm):
    class Meta:
        model = Telefonia
        fields = ['situacao', 'descricao']



