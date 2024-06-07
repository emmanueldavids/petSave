from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Donation



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user



class DonationForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    AMOUNT_CHOICES = [
        ('$10', '$10'),
        ('$20', '$20'),
        ('$30', '$30'),
        ('$40', '$40'),
        ('$50', '$50'),
        ('$60', '$60'),
        ('$70', '$70'),
        ('$80', '$80'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.ChoiceField(choices=AMOUNT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Donation
        fields = ['full_name', 'email', 'country', 'gender', 'amount', 'city', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'placeholder': 'Any message for Us'}),
        }
