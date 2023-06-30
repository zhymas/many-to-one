from django import forms
from django.forms import ModelForm
from .models import *


class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = ['firs_name', 'last_name', 'email']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'pub_date', 'reporter']

        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            'headline': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
