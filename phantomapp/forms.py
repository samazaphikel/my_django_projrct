from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '35'}),label='username')
	password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'special', 'size': '35'}), min_length=8, max_length=100,label='password')

	class Meta:
		model = User
		fields = ('username','password1')

