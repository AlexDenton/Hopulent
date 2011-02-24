from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms
from django.template import RequestContext

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput)

def user(request, username):
	age = request.user.profile.age
	return HttpResponse(age)

def authenticate(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponse('Sucess!') 
		else:
			return HttpResponse('Account disabled.')
	else:
		return HttpResponse('Invalid login.')
			
	
def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			# process data
			return render_to_response('win.html')
		
	else:
		form = LoginForm()
		render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
			
	return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
	
	
