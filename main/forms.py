from django.forms import ModelForm
from main.models import Book, Author


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors', 'publication']


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'gender']
