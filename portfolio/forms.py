from django import forms
from django.db import models
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('photo','title', 'description','tags','url')
