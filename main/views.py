# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from main.models import Book, Author
from main.forms import BookForm, AuthorForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class BookListView(MyLoginRequiredMixin, View):

    def get(self, request):
        books = Book.get_all()

        return render(request, "book_list.html", context={
            "books": books
        })


class BookAddView(MyLoginRequiredMixin, View):

    def get(self, request):
        form = BookForm()
        return render(request, 'book_add.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/')

        return render(request, 'book_add.html', {'form': form})


class BookEditView(MyLoginRequiredMixin, View):

    def get(self, request, id):
        book = Book.objects.get(id=id)
        form = BookForm(instance=book)

        return render(request, 'book_add.html', {'form': form})

    def post(self, request, id):
        book = Book.objects.get(id=id)
        form = BookForm(request.POST, instance=book)
        form.id = id
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/')

        return render(request, 'book_add.html', {'form': form})


class BookDeleteView(MyLoginRequiredMixin, View):

    def get(self, request, id):
        book = Book.objects.get(id=id)

        return render(request, 'book_delete.html', {'book': book})

    def post(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()

        return HttpResponseRedirect('/books/')


class AuthorListView(MyLoginRequiredMixin, View):

    def get(self, request):
        authors = Author.get_all()

        return render(request, "author_list.html", context={
            "authors": authors
        })


class AuthorAddView(MyLoginRequiredMixin, View):

    def get(self, request):
        form = AuthorForm()
        return render(request, 'author_add.html', {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/authors/')

        return render(request, 'author_add.html', {'form': form})


class AuthorEditView(MyLoginRequiredMixin, View):

    def get(self, request, id):
        author = Author.objects.get(id=id)
        form = AuthorForm(instance=author)

        return render(request, 'author_add.html', {'form': form})

    def post(self, request, id):
        author = Author.objects.get(id=id)
        form = AuthorForm(request.POST, instance=author)
        form.id = id
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/authors/')

        return render(request, 'author_add.html', {'form': form})


class AuthorDeleteView(MyLoginRequiredMixin, View):

    def get(self, request, id):
        author = Author.objects.get(id=id)

        return render(request, 'author_delete.html', {'author': author})

    def post(self, request, id):
        author = Author.objects.get(id=id)
        author.delete()

        return HttpResponseRedirect('/authors/')

