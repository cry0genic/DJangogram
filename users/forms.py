from django import forms
from django.contrib.auth.models import User
from .models import Profile
from blog.models import Comment, Post
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta: 
		model = User
		fields = ['username', 'email', 'password1', 'password2'] 

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

		
class ProfileUpdateForm(forms.ModelForm): 

	class Meta:						
		model = Profile
		fields = ['image']

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ['content']

class PostCreateForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ['title', 'content']

