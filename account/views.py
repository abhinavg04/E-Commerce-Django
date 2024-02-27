from django.shortcuts import render,redirect
from django.views import View
from .forms import RegForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def intro(request):
    return render(request,'landing.html')

class LoginView(View):
    def get(self,request):
        logform = LoginForm()
        return render(request,'login.html',{'form':logform})
    def post(self,request):
        form_data = LoginForm(data=request.POST)
        if form_data.is_valid():
            uname = form_data.cleaned_data.get('Username')
            pswd = form_data.cleaned_data.get('Password')
            user = authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,'Login Successfull')
                return redirect('userhome')
            else:
                messages.error(request,'Login Failed')
                return redirect('login')
        else:
            return render(request,'login.html',{'form':form_data})
class RegView(View):
    def get(self,request):
        regform = RegForm()
        return render(request,'reg.html',{'form':regform})
    def post(self,request):
        form_data = RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Signup Successfull')
            return redirect('login')
        else:
            return render(request,'login.html',{'form':form_data})
        
def logout_user(request):
    logout(request)
    return redirect('landing')

def user_page(request):
    return render(request,'user_page.html')