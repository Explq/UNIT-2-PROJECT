from django import forms
from .models import Project, ContactMessage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search',max_length=100, required=False)

    def clean_query(self):
        query = self.cleaned_data.get('query')
        if query:
            return query.strip().lower()
        return query

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }