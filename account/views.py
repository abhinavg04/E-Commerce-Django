from django.shortcuts import render,redirect
from django.views import View
from .forms import RegForm,LoginForm,UpdateUserForm,ChangePassword
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView,TemplateView
from django.contrib.auth.models import User
# Create your views here.

# generic template view
class Intro(TemplateView):
    template_name='landing.html'

# generic form view
class LoginView(FormView):
    form_class=LoginForm
    template_name='login.html'
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
# class RegView(View):
#     def get(self,request):
#         regform = RegForm()
#         return render(request,'reg.html',{'form':regform})
#     def post(self,request):
#         form_data = RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,'Signup Successfull')
#             return redirect('login')
#         else:
#             return render(request,'login.html',{'form':form_data})
        
# generic view createView
class RegView(CreateView):
    form_class=RegForm
    template_name='reg.html'
    success_url=reverse_lazy('login')
        
def logout_user(request):
    logout(request)
    return redirect('landing')

def user_page(request):
    return render(request,'user_page.html')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        update_form = UpdateUserForm(request.POST or None,instance=current_user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request,'Successfully updated')
            return redirect('user_page')
        else:
            return render(request,'update_user.html',{'form':update_form})
    return render(request,'update_user.html',{'form':update_form})


class UpdatePassword(View):
    def get(self,request):
        if request.user.is_authenticated:
            current_user = request.user
        form = ChangePassword(current_user)
        return render(request,'update_password.html',{'form':form})
    def post(self,request):
        if request.user.is_authenticated:
            current_user = request.user
        form = ChangePassword(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated')
            return redirect('login')
        else:    
            return render(request,'update_password.html',{'form':form})


