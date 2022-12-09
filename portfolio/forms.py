from django import forms
from django.db import models
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('photo','title', 'description','tags','url')

'''photo = forms.ImageField() #(que puede ser una URL)
    title = forms.TextInput() # Project Title
    description = forms.Textarea() # Project Description
    tags = forms.TextInput() # HTML, CSS, PYTHON, etc
    url = forms.TextInput() # URL de github'''
    
'''class Meta:
        model = Portfolio
        fields = ('photo','title','description','tags','url')
        
        widgets = {
            'photo' : forms.FileInput(attrs={'class':'form-control'}),
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'tags' : forms.TextInput(attrs={'class':'form-control'}),
            'url' : forms.TextInput(attrs={'class':'form-control'}),
        }'''