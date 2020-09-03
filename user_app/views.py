# Import Required Functions, Classes and Decorators
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Homepage Views
@login_required(login_url='login')
def homepage(request):
    return render(request, 'Blogs/index.html', {})

# Register Views
def register(request):

    # Creating Custom Form
    form = UserRegisterForm()
    # IF Request is POST Only
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Validating the Form
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"{username}, Your Account is Created!")
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'user_app/register.html', context)

# Login View
def loginForm(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # User Authentication
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, f'Your Username or Password is incorrect!!!')

    context = {}
    return render(request, 'user_app/login.html', context)

# Logout View
def logoutView(request):
    logout(request)
    return redirect('login')