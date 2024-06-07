from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .forms import DonationForm




from django.contrib import messages

def index(request):
    # tasks = Task.objects.all()
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the form data to the database
            return redirect('dashboard')  # Redirect to a success page or wherever you want
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'donation_list.html', {'donations': donations})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)

            messages.success(request, "Account was created for " + username)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('donate')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
