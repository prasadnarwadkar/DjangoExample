from django import urls
from django.contrib import admin
from django.urls import include, path, re_path

from django.conf.urls.static import static

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from mysite import settings
from sqlite3reader import views
from django.contrib.auth.views import LoginView, LogoutView
from home import views as HomeViews

app_name = 'sqlite3reader'
urlpatterns = [
    path("", views.index, name="Landing"),
    path('Homepage/', HomeViews.index, name='Homepage'),
    path(
        "favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))
    )
]
