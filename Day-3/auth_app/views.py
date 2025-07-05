from django.shortcuts import render, redirect


# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm


def login_view(request):

    if request.user.is_authenticated:
        return redirect('home-index')
    else:    
        if request.method == 'POST':
            uname = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=uname, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('bookstore:bookstore-index')
            else:
                messages.info(request, "User name or password is incorrect")

    return render(request, 'main/login.html')

def signout(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('bookstore:bookstore-index')
    else:
        signup_form = UserForm()
        if request.method == 'POST':
            signup_form = UserForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                msg = "User account created for username: " + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
    
    context = {"signup_form": signup_form}
    return render(request, 'main/signup.html', context=context)