from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from .models import Profile

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST) #Creates the form with the data contained in request.POST
		if form.is_valid():
			form.save()
			messages.success(request, 'Your account has been created. You can now login!')
			return redirect('login') 
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form, 'title': 'Register'})

@login_required #Decorator to make sure this view is blocked for those not logged in
def profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, 'Profile updated successfully')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)

