"""MyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'books/$', views.BookListView.as_view()),
    url(r'add-book/$', views.BookAddView.as_view()),
    url(r'edit-book/(?P<id>\d+)/$', views.BookEditView.as_view()),
    url(r'delete-book/(?P<id>\d+)/$', views.BookDeleteView.as_view()),

    url(r'authors/$', views.AuthorListView.as_view()),
    url(r'add-author/$', views.AuthorAddView.as_view()),
    url(r'edit-author/(?P<id>\d+)/$', views.AuthorEditView.as_view()),
    url(r'delete-author/(?P<id>\d+)/$', views.AuthorDeleteView.as_view()),
]
