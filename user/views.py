from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView
from account.models import Products
# Create your views here.

class ProductDetails(ListView):
    template_name='product_details.html'
    queryset=Products.objects.all()
    context_object_name='products'

class UserHome(View):
    def get(self,request):
        random_obj = Products.objects.all().order_by('?')[:6]
        return render(request,'userhome.html',{'products':random_obj})
    
# def category(request,category):
#     products = Products.objects.filter(category=category)
#     return render(request,'category_item_list.html',{'products':products})

class Category(ListView):
    template_name='category_item_list.html'
    queryset=Products.objects.all()
    context_object_name='products'
    def get_context_data(self, **kwargs):
        res = Products.objects.filter(category=self.kwargs.get('category')) 
        return {'products':res}
        
