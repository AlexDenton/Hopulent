from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.Form):
        username = forms.CharField(max_length=20)
        email = forms.EmailField(max_length=40)
        password = forms.CharField(max_length=20, widget=forms.PasswordInput)
 #       confirm = forms.CharField(max_length=20, widget=forms.PasswordInput)
 #       gender = forms.ChoiceField(widget=forms.RadioSelect(choices=(('male','MALE'),('no','NO'))), required=True)
              
def signup(request):
        user = request.user
        if request.method == 'POST':
                signupForm = SignupForm(request.POST)
                if signupForm.is_valid():
                        username = signupForm.cleaned_data['username']
                        email = signupForm.cleaned_data['email']
                        password = signupForm.cleaned_data['password']
        #                confirm = signupForm.cleaned_data['confirm']
        #                gender = singupForm.cleaned_data['gender']
                        user = User.objects.create_user('username','email','password')
                        return render_to_response('signup/activated.html',{'signupForm':signupForm}, context_instance=RequestContext(request))                                
                        
        else:
                signupForm = SignupForm()
                return render_to_response('signup/signup.html',{'signupForm':signupForm}, context_instance=RequestContext(request))                                

        return render_to_response('signup/signup.html',{'signupForm':signupForm}, context_instance=RequestContext(request))

