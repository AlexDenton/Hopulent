from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext
from django.contrib.auth import authenticate, login

class SearchForm(forms.Form):
	query = forms.CharField(max_length=40, required=False)

class SigninForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput)

def main_page(request):
	user = request.user
	if request.method == 'POST':
		signinForm = SigninForm(request.POST)
		searchForm = SearchForm(request.POST)
		if signinForm.is_valid():			
			username = signinForm.cleaned_data['username']
			password = signinForm.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return render_to_response('index/index.html', {'signinForm': signinForm, 'searchForm': searchForm}, context_instance=RequestContext(request))
			else:
				return render_to_response('index/index.html', {'signinForm': signinForm, 'searchForm': searchForm}, context_instance=RequestContext(request))
	else:
		signinForm = SigninForm()
		searchForm = SearchForm()
		render_to_response('index/index.html', {'signinForm': signinForm, 'searchForm': searchForm, 'user': user}, context_instance=RequestContext(request))
			
	return render_to_response('index/index.html', {'signinForm': signinForm, 'searchForm': searchForm}, context_instance=RequestContext(request))
