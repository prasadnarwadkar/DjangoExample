from django.urls import path

from .views import SignUpView, password_change_view
from home import views as HomeViews

urlpatterns = [
    path('Homepage/', HomeViews.index, name='Homepage'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("password_change/", password_change_view, name="password_change")
]
