from django import forms
from django.forms import ModelForm
from .models import figus_totales
class agregarFigurita(ModelForm):
    class Meta:
        model = figus_totales
        fields = ['num_figu', 'type']

class filtrarFigurita(ModelForm):
    class Meta:
        model = figus_totales
        fields = ['type']