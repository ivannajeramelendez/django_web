from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# from .models import Question, Choice
#==========================[ DASHBOARD ]==========================#
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth import logout
from .forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm

#==========================[ PAGES ]==========================#
def inicio(request):
  return render(request, 'pages/index.html', { 'segment': 'index' })

def perfil(request):
  return render(request, 'pages/profile.html', { 'segment': 'perfil' })

def aforos(request):
  return render(request, 'aforos/menu.html', { 'segment': 'aforos' })

# def billing(request):
#   return render(request, 'pages/billing.html', { 'segment': 'billing' })

# def tables(request):
#   return render(request, 'pages/tables.html', { 'segment': 'tables' })

# def vr(request):
#   return render(request, 'pages/virtual-reality.html', { 'segment': 'vr' })

# def rtl(request):
#   return render(request, 'pages/rtl.html', { 'segment': 'rtl' })

# def profile(request):
#   return render(request, 'pages/profile.html', { 'segment': 'profile' })

#==========================[ Authentication ]==========================#
class UserLoginView(LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Register failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/register.html', context)

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')