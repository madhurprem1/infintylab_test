# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MyMetaModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Author(MyMetaModel):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    name = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=False)

    @classmethod
    def get_all(cls):
        return Author.objects.all()

    def __str__(self):
        return "Author: {name}".format(name=self.name)


class Book(MyMetaModel):
    name = models.CharField(max_length=100, null=False)
    authors = models.ManyToManyField(Author, related_name='Books')
    publication = models.CharField(max_length=100, null=True, blank=True)

    @classmethod
    def get_all(cls):
        return Book.objects.prefetch_related('authors').all()

    def __str__(self):
        return "Book: {name}".format(name=self.name)

