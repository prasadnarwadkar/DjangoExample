"""
URL configuration for consume_restful_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import include, path, re_path

from django.conf.urls.static import static

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from mysite import settings
from heroes import views
from django.contrib.auth.views import LoginView, LogoutView
from home import views as HomeViews

app_name = 'heroes'
urlpatterns = [ 
    

    path('details/<uuid:id>', views.details, name='Avenger-details'),
    path('delete/<uuid:id>', views.delete, name='Avenger-delete'),
    path('new/', views.new, name='new'),
    path('Homepage/', HomeViews.index, name='Homepage'),
    path('', views.heroes, name='Landing'),
    
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('login/', views.loginView, name='login'),
    
    path('logout/', views.logoutView, name='logout'), 
]