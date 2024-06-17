# from django.db import models
# from django.contrib.auth.models import User

# class Transaction(models.Model):
#     sender = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE)
#     recipient = models.ForeignKey(User, related_name='received_transactions', on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     # Add more fields as per your requirements

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


# from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

# class Transaction(models.Model):
#     sender = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE)
#     recipient = models.ForeignKey(User, related_name='received_transactions', on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     timestamp = models.DateTimeField(auto_now_add=True)


# payments/models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=(('Pending', 'Pending'), ('Completed', 'Completed')))

# transactions/models.py
from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction to {self.user.username} - ${self.amount}"
