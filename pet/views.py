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
    user = request.user

    form = DonationForm()

    # Handle donation form submission
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
        # Calculate user's balance
            transactions = Transaction.objects.filter(user=user)
            previous_balance = sum(transaction.amount for transaction in transactions)
            new_balance = previous_balance - amount
            # donated_amount = amount - balance

            # Ensure user has sufficient balance
            if new_balance < 0:
                context = {
                    'form': form,
                    'page_obj': page_obj,
                    'balance': previous_balance,
                    'error_message': 'Insufficient funds',
                }
                return render(request, 'dashboard.html', context)

                # Deduct amount from user's wallet balance
                user.balance -= amount
                user.save()


            # Create a new donation record
            Donation.objects.create(user=user, amount=amount)
            # Create a new transaction record (negative to indicate deduction)
            Transaction.objects.create(user=user, amount=-amount)

            return redirect('dashboard')  # Redirect to refresh the page

    donations = Donation.objects.all() # Order by 'id' field to ensure consistency
    paginator = Paginator(donations, 5)  # Show 5 donations per page

    # Calculate user's balance
    transactions = Transaction.objects.filter(user=user)
    balance = sum(transaction.amount for transaction in transactions)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    user = request.user


    context = {
        'page_obj': page_obj,
        'money': balance,
        'previous_balance': balance + form['amount'].value() if 'amount' in form.data else balance,
        'donated_amount': form['amount'].value() if 'amount' in form.data else 0,
        # 'new_balance': new_balance,
    }
    return render(request, 'dashboard.html', context)


def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the form data to the database
            # messages.success(request, "Account was created for " + email)

            # if user_profile.wallet_balance >= amount:
            #     user_profile.wallet_balance -= amount
            #     user_profile.save()
            #     return Response({'status': 'Money sent successfully!'})
            # else:
            #     return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
            return redirect('dashboard')  # Redirect to a success page or wherever you want
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})


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
