from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
import requests

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def password_change_view(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(user=request.user, data=request.POST)
        if pass_form.is_valid():
            pass_form.save()
            success_url = reverse_lazy("login")
            return redirect(success_url)
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/password_change.html', {'password_form': pass_form})
    
