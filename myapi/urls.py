# transactions/urls.py
from django.urls import path
from .views import TransactionListCreate, TransactionDetail

urlpatterns = [
    path('transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
]
