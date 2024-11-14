from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search',max_length=100, required=False)
