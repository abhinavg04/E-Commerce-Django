from django.shortcuts import render
from django.views import View
from account.models import Products
# Create your views here.
class UserHome(View):
    def get(self,request):
        random_obj = Products.objects.all().order_by('?')[:6]
        return render(request,'userhome.html',{'products':random_obj})
    
def category(request,category):
    products = Products.objects.filter(category=category)
    return render(request,'category_item_list.html',{'products':products})
        
