from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.localflavor.us.forms import USStateField
from models import UserProfile
from django.utils.hashcompat import sha_constructor
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
import smtplib
import random
from random import choice
import datetime

choices = (('male','male'),('female','female'),)

class SignupForm(forms.Form):
       # username = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=30)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput)
	confirm = forms.CharField(max_length=20, widget=forms.PasswordInput)
#	first_name = forms.CharField(max_length=20)
#	last_name = forms.CharField(max_length=20)
#	city = forms.CharField(max_length=10)
#	state = USStateField()
	birthday = forms.DateField()
#       gender = forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
	captcha = forms.IntegerField()
	n1, n2 = random.randint(1,6), random.randint(1,6) 
	if n2>n1:
		n1,n2 = n2,n1
	operator =  choice(u'+-')
	math_equation = "%s %s %s" % (n1, operator , n2)
	if operator == '+':
		n3 = n1+n2
	if operator == '-':
		n3 = n1-n2 
	captcha.label = math_equation


class SigninForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class editProfileForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20, widget=forms.PasswordInput)
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=30)
	city = forms.CharField(max_length=10)
	state = USStateField()
	birthday = forms.DateField()
	gender = forms.ChoiceField(choices=choices,widget=forms.RadioSelect)
#	profPic = 
	
def signin(request):
	if request.method == 'POST':
		signinForm = SigninForm(request.POST)
		if signinForm.is_valid():			
			username = signinForm.cleaned_data['username']
			password = signinForm.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return render_to_response('index/index.html', {'signinForm': signinForm}, context_instance=RequestContext(request))
	else:
		signinForm = SigninForm()
		return render_to_response('index/index.html', {'signinForm': signinForm}, context_instance=RequestContext(request))
		
	return render_to_response('index/index.html', {'signinForm': signinForm}, context_instance=RequestContext(request))
	
def signout(request):
	logout(request)
	return redirect('/')

def user_profile(request, user_id):
	user = User.objects.get(pk=user_id)
	return render_to_response('account/userprofile.html', {'user': user}, context_instance=RequestContext(request))

def signup(request):
        user = request.user
	profile = UserProfile()
        if request.method == 'POST':
            	random.random()
		signupForm = SignupForm(request.POST)
		if signupForm.is_valid():       	
			if signupForm.cleaned_data['captcha'] == SignupForm.n3: 			
				email = signupForm.cleaned_data['email']
				username = email.split('@', 1 )[0]
		 		password = signupForm.cleaned_data['password']
				confirm = signupForm.cleaned_data['confirm']
				if confirm != password:
					signupForm.confirm = ''	
					return render_to_response('account/confirmError.html',{'signupForm':signupForm}, context_instance=RequestContext(request))
#				first_name = signupForm.cleaned_data['first_name']
#				last_name = signupForm.cleaned_data['last_name']
#               	        profile.city = signupForm.cleaned_data['city']
#				profile.state = signupForm.cleaned_data['state']
				profile.birthday = signupForm.cleaned_data['birthday']
				month = profile.birthday.month
				day = profile.birthday.day			
				year = profile.birthday.year
				now = datetime.datetime.now()
				if now.year - year < 21:
					return render_to_response('account/ageError.html',{'signupForm':signupForm}, context_instance=RequestContext(request))
				if now.year - year == 21:
					if now.month < month:	
						return render_to_response('account/ageError.html',{'signupForm':signupForm}, context_instance=RequestContext(request))
					if now.month == month:	
						if now.day < day:
							return render_to_response('account/ageError.html',{'signupForm':signupForm}, context_instance=RequestContext(request))	
	
#       	                profile.gender = signupForm.cleaned_data['gender']
	               	        user = User.objects.create_user(username,email,password)	
#				user.first_name = first_name
#				user.last_name = last_name
				user.is_active = False
				user.save()
				salt = sha_constructor(str(random.random())).hexdigest()[:5]
				activation_key = sha_constructor(salt+user.username).hexdigest()
				ctx_dict  = {'activation_key': activation_key }
				subject = render_to_string('account/activation_email_subject.txt',ctx_dict)
				subject = ''.join(subject.splitlines())
				message = render_to_string('account/activation_email.txt', ctx_dict)	
#				user.email_user(subject, message, from_email=None)
				profile.user = user
				profile.save()
                
			        return render_to_response('account/activated.html',{'signupForm':signupForm}, context_instance=RequestContext(request))                 
			else:
				signupForm.captcha = ''
				return render_to_response('account/captchaError.html',{'signupForm':signupForm}, context_instance=RequestContext(request))
        else:
                signupForm = SignupForm()
              
	  	return render_to_response('account/signup.html',{'signupForm':signupForm}, context_instance=RequestContext(request))                            
 
	return render_to_response('account/signup.html',{'signupForm':signupForm}, context_instance=RequestContext(request))        
