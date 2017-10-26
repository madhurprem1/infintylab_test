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


class MyEditView(MyLoginRequiredMixin, View):
    model = None
    model_form = None
    redirect_to = ''
    template_name = ''

    def get(self, request, id):
        instance = self.model.objects.get(id=id)
        form = self.model_form(instance=instance)

        return render(request, 'book_add.html', {'form': form})

    def post(self, request, id):
        instance = self.model.objects.get(id=id)
        form = self.model_form(request.POST, instance=instance)
        form.id = id
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.redirect_to)

        return render(request, self.template_name, {'form': form})


class MyAddView(MyLoginRequiredMixin, View):
    model = None
    model_form = None
    redirect_to = ''
    template_name = ''

    def get(self, request):
        form = self.model_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.model_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.redirect_to)

        return render(request, self.template_name, {'form': form})


class MyDeleteView(MyLoginRequiredMixin, View):
    model = None
    model_form = None
    redirect_to = ''
    template_name = 'delete.html'

    def get(self, request, id):
        instance = self.model.objects.get(id=id)

        return render(request, self.template_name, {
            'name': instance.name,
            'redirect_to': self.redirect_to,
            'model_name': self.model._meta.model_name
        })

    def post(self, request, id):
        instance = self.model.objects.get(id=id)
        instance.delete()

        return HttpResponseRedirect(self.redirect_to)


class BookListView(MyLoginRequiredMixin, View):

    def get(self, request):
        books = Book.get_all()

        return render(request, "book_list.html", context={
            "books": books
        })


class BookAddView(MyAddView):
    model = Book
    model_form = BookForm
    redirect_to = '/books/'
    template_name = 'book_add.html'


class BookEditView(MyEditView):
    model = Book
    model_form = BookForm
    redirect_to = '/books/'
    template_name = 'book_add.html'


class BookDeleteView(MyDeleteView):
    model = Book
    model_form = BookForm
    redirect_to = '/books/'


class AuthorListView(MyLoginRequiredMixin, View):

    def get(self, request):
        authors = Author.get_all()

        return render(request, "author_list.html", context={
            "authors": authors
        })


class AuthorAddView(MyAddView):
    model = Author
    model_form = AuthorForm
    redirect_to = '/authors/'
    template_name = 'author_add.html'


class AuthorEditView(MyEditView):
    model = Author
    model_form = AuthorForm
    redirect_to = '/authors/'
    template_name = 'author_add.html'


class AuthorDeleteView(MyDeleteView):
    model = Author
    model_form = AuthorForm
    redirect_to = '/authors/'
