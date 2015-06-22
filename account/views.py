from django.contrib.auth.hashers import make_password, check_password
from django.views.generic.base import View
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from account.forms import SignUpForm, LoginForm
from account.models import User
from blog.models import Blog



class IndexView(View):
    form = SignUpForm
    template_name = "index.html"
    fa = {'username':'fa-user','email':'fa-envelope-o'}

    def get(self, request, *args, **kwargs):
        form = self.form()
        fa = self.fa
        return render(request, self.template_name, {'form': form, 'fa':fa})

    def post(self,request,*args,**kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            _username = form.cleaned_data['username']
            _email = form.cleaned_data['email']
            _password = form.cleaned_data['password']
            if _password and _password == form.cleaned_data['passwordConfirm']:
                user = User(username=_username,email=_email,password=make_password(_password,None,'pbkdf2_sha256'),date_joined = timezone.now())
                blog = Blog(username=_username,created_date = timezone.now(),is_active=1,is_locked=0)
                user.save()
                blog.save()

class LoginView(View):
    form = LoginForm
    template = "login.html"
    fa = {'username':'fa-user','password':'fa-unlock-alt'}
    def get(self,request, *args,**kwargs):
        form = self.form()
        fa = self.fa
        return render(request,self.template, {'form':form, 'fa':fa})

    def post(self,request,*args,**kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            _username = form.cleaned_data['username']
            _password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=_username)
                if user:
                    if check_password(_password,user.password):
                        return HttpResponse('login success')
                    else:
                        return HttpResponse('wrong password')
            except User.DoesNotExist:
                return HttpResponse('no such id')
        else:
            return render(request,self.template, {'form':self.form()})

