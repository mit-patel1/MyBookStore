from django import forms
from .models import Books, BookImage

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'description', 'author', 'category', 'purchase_link']


class BookImageForm(forms.ModelForm):
    class Meta:
        model = BookImage
        fields = ['image']

