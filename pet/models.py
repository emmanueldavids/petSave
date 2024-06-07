# models.py
from django.db import models

class Donation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    amount = models.CharField(max_length=10, choices=[('$10', '$10'), ('$20', '$20'), ('$30', '$30'), ('$40', '$40'), ('$50', '$50'), ('$60', '$60'), ('$70', '$70'), ('$80', '$80')])
    city = models.CharField(max_length=100)
    message = models.TextField(blank= True, null = True)

    def __str__(self):
        return f"Donation by {self.full_name}"
    # amount = models.DecimalField(max_digits=10, decimal_places=2)
