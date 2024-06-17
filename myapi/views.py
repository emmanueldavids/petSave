# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .models import Transaction
# from .serializers import TransactionSerializer

# class SendMoneyView(generics.CreateAPIView):
#     serializer_class = TransactionSerializer
#     # permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         sender = self.request.user
#         recipient_id = self.request.data.get('recipient_id')
#         amount = self.request.data.get('amount')

#         # Perform validations, update balances, create transaction, handle exceptions

#         serializer.save(sender=sender, recipient_id=recipient_id, amount=amount)


# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
# from .models import Transaction, UserProfile
# from .serializers import TransactionSerializer

# class SendMoneyView(generics.CreateAPIView):
#     serializer_class = TransactionSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         sender = self.request.user
#         recipient_id = self.request.data.get('recipient_id')
#         amount = self.request.data.get('amount')

#         try:
#             amount = float(amount)
#         except ValueError:
#             return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             recipient = User.objects.get(id=recipient_id)
#         except User.DoesNotExist:
#             return Response({"error": "Recipient does not exist"}, status=status.HTTP_404_NOT_FOUND)

#         sender_profile = sender.userprofile
#         recipient_profile = recipient.userprofile

#         if sender_profile.balance >= amount:
#             sender_profile.balance -= amount
#             recipient_profile.balance += amount
#             sender_profile.save()
#             recipient_profile.save()

#             serializer.save(sender=sender, recipient=recipient, amount=amount)
#         else:
#             return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)


# views.py

# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
# from .models import Transaction, UserProfile
# from .serializers import TransactionSerializer

# import logging

# logger = logging.getLogger(__name__)

# class SendMoneyView(generics.CreateAPIView):
#     serializer_class = TransactionSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         sender = self.request.user
#         recipient_id = self.request.data.get('recipient_id')
#         amount = self.request.data.get('amount')

#         try:
#             amount = float(amount)
#         except ValueError:
#             raise ValueError("Invalid amount")

#         try:
#             recipient = User.objects.get(id=recipient_id)
#         except User.DoesNotExist:
#             raise ValueError("Recipient does not exist")

#         sender_profile = sender.userprofile
#         recipient_profile = recipient.userprofile

#         if sender_profile.balance >= amount:
#             sender_profile.balance -= amount
#             recipient_profile.balance += amount
#             sender_profile.save()
#             recipient_profile.save()

#             transaction = serializer.save(sender=sender, recipient=recipient, amount=amount)
#             return transaction
#         else:
#             raise ValueError("Insufficient balance")

# payments/views.py
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User
# from .models import Transaction
# from .serializers import TransactionSerializer

# class SendMoneyView(generics.CreateAPIView):
#     serializer_class = TransactionSerializer

#     def create(self, request, *args, **kwargs):
#         user_id = request.data.get('user_id')
#         amount = request.data.get('amount')
#         user = User.objects.get(id=user_id)
#         transaction = Transaction.objects.create(user=user, amount=amount, status='Completed')
#         serializer = self.get_serializer(transaction)
#         money.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# # Assuming you have a UserProfile model linked to the User model where balance is stored
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .models import Transaction

# @login_required
# def dashboard(request):
#     # Fetch the user's profile or balance information
#     transaction = Transaction.objects.get(user=request.user)  # Assuming UserProfile is linked to User
#     balance = transaction.balance

#     context = {
#         'balance': balance,
#     }
#     return render(request, 'dashboard.html', context)


# transactions/views.py
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer



# transactions/views.py
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .models import Transaction

# @login_required
# def dashboard(request):
#     user = request.user
#     transactions = Transaction.objects.filter(user=user)
#     balance = sum(transaction.amount for transaction in transactions)
    
#     context = {
#         'money': balance
#     }
#     return render(request, '../pet/templates/dashboard.html', context)


# localhost/api
# GET /api/transactions/<id>/
# PUT /api/transactions/<id>/
# DELETE /api/transactions/<id>/