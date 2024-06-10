from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .forms import DonationForm
from .models import Donation
from django.core.paginator import Paginator


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


# def dashboard(request):
#     donations = Donation.objects.all().order_by('id')
#     paginator = Paginator(dashboard, 10)  # Show 10 donations per page

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'page_obj': page_obj,
#     }


#     return render(request, 'dashboard.html', {'donations': donations}, {'page_obj':page_obj})
def dashboard(request):
    donations = Donation.objects.all() # Order by 'id' field to ensure consistency
    paginator = Paginator(donations, 5)  # Show 10 donations per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'dashboard.html', context)
    # return render(request, 'dashboard.html', {'page_obj': page_obj})

    # return render(request, 'dashboard.html', {'donations': donations})


def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the form data to the database
            # messages.success(request, "Account was created for " + email)
            return redirect('dashboard')  # Redirect to a success page or wherever you want
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})


# def donation_list(request):
    

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

