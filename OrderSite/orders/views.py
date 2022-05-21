from datetime import datetime

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib import messages
import hashlib

from orders.forms import AuthUserForm
from orders.models import Users


class SiteView(ListView):
    template_name = 'base.html'
    context_object_name = 'orders'


def index(request):
    return render(request, 'base.html')


class SiteLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index')

def registerPage(request):
    if request.method == 'POST':
        user = User()
        user.first_name = request.POST.get("FirstName")
        user.last_name = request.POST.get("LastName")
        user.email = request.POST.get("Email")
        user.username = request.POST.get("Login")
        user.set_password(request.POST.get("Password"))
        user.save()
        context = {
            'form': f"<div class='alert {{ message.tags }} text-center m-2' id='msg' role='alert'>Регистрация успешно завершена. Здравствуйте,'{user.first_name} {user.last_name}!Добро пожаловать</div>:"}
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return render(request, 'base.html', context)


class Logout(LogoutView):
    next_page = reverse_lazy('index')
