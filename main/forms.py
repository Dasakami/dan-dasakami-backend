from django import forms
from .models import Article, Contacts
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'cover']


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'subject', 'message']


