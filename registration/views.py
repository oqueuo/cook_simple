"""
Views for registration app

register: Allows user to pick a username and password to create an account.
          Uses the default UserCreationForm from Django
"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(response, 'registration/register.html', {'form':form})
