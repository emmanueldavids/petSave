from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .forms import DonationForm
from .models import Donation
from django.core.paginator import Paginator
from myapi.models import Transaction

from django.contrib import messages


def index(request):
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
    donations = Donation.objects.all() # Order by 'id' field to ensure consistency
    paginator = Paginator(donations, 5)  # Show 5 donations per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        #  'money': balance,
    }
    user = request.user
    transactions = Transaction.objects.filter(user=user)
    balance = sum(transaction.amount for transaction in transactions)
    
    context1 = {
        'money': balance
    }
    return render(request, 'dashboard.html', context)


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
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# #API
# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from myapi.models import UserProfile
# from myapi.serializers import UserSerializer, UserProfileSerializer
# from django.contrib.auth.decorators import login_required



# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     @action(detail=True, methods=['post'])
#     def send_money(self, request, pk=None):
#         user = self.get_object()
#         amount = request.data.get('amount')
#         try:
#             amount = float(amount)
#         except ValueError:
#             return Response({"error": "Invalid amount"}, status=400)

#         user.profile.wallet_balance += amount
#         user.profile.save()
#         return Response({"status": "money sent", "new_balance": user.profile.wallet_balance})

#     @login_required
#     def wallet_view(request):
#         user_profile = UserProfile.objects.get(user=request.user)
#         wallet_balance = user_profile.wallet_balance
#         return render(request, 'wallet.html', {'wallet_balance': wallet_balance})