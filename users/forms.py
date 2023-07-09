# from django import forms
# from django.contrib.auth.forms import UserCreationForm
from profiles_api.models import UserProfile

# class SignupForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = UserProfile
#         fields = ('email', 'name', 'password')

# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'password1', 'password2')