from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput)

def user(request, username):
	age = request.user.profile.age
	return HttpResponse(age)
	
def loginify(request, username, password):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return render_to_response('account/win.html')
			else:
				return render_to_response('account/fail.html')
	else:
		form = LoginForm()
		render_to_response('account/login.html', {'form': form}, context_instance=RequestContext(request))
			
	return render_to_response('account/login.html', {'form': form}, context_instance=RequestContext(request))
	
	
