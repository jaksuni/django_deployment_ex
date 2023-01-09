from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfoForms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfoForms
		fields = ('portfolio_site',  'profile_pic')