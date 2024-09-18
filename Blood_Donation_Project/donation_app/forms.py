from django import forms
from .models import CustomUser, Profile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']

REGION_CHOICES = [
    ('Region I', 'Region I'),
    ('Region III', 'Region III'),
]

PROVINCE_CHOICES = [
    ('Pampanga', 'Pampanga'),
    ('Tarlac', 'Tarlac'),
]

MUNICIPALITY_CHOICES = [
    ('Angeles', 'Angeles'),
    ('San Fernando', 'San Fernando'),
]

class ProfileForm(forms.ModelForm):
    region = forms.ChoiceField(choices=REGION_CHOICES)
    province = forms.ChoiceField(choices=PROVINCE_CHOICES)
    municipality = forms.ChoiceField(choices=MUNICIPALITY_CHOICES)
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'blood_type', 'availability']





