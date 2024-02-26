from django.shortcuts import render
from django.views import View
# Create your views here.
class UserHome(View):
    def get(self,request):
        return render(request,'userhome.html')