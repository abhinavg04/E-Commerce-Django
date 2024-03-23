from typing import Any
from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,DeleteView
from account.models import Products,Cart,Review,Orders
from django.contrib import messages
from django.core.mail import send_mail
from account.views import dec
from django.utils.decorators import method_decorator
import csv
# Create your views here.

def review_summary(request,id):
     review = Review.objects.filter(products_id=id)
     print(review)
     with open('review.csv','w',newline='') as revcsv:
        csvwriter = csv.writer(revcsv)
        csvwriter.writerow(["id","review","date","product_id","user_id"])
        for i in review:
            csvwriter.writerow([i.id,i.review,i.date,i.products.id,i.user.id])
     return render(request,'review_summary.html')

dec
def cancelorder(request,**kwargs):
    oid=kwargs.get('oid')
    order=Orders.objects.get(id=oid)
    order.order_status="Cancelled"
    order.save()
    #mail service
    to_mail=request.user.email
    msg=f"Order for the request {order.products.title} is cancelled successfully!! Check your ecommerce account for more details"
    from_mail="abhinavg1024@gmail.com"
    subject="Order Cancellation Confirmation"
    send_mail(subject,msg,from_mail,[to_mail])
    return redirect('order')

@method_decorator(dec,name='dispatch')
class Order(ListView):
    template_name='order.html'
    queryset = Orders.objects.all()
    context_object_name='order'
    def get_queryset(self):
        res=super().get_queryset()
        # print(self.request.session)
        res=res.filter(user=self.request.user)
        return res
@method_decorator(dec,name='dispatch')   
class Checkout(View):
    def get(self,request):
        cart = Cart.objects.filter(user=request.user)
        sum = 0
        for i in cart:
            if i.products.is_offer:
                sum+= i.products.offer_price
            else:
                sum+=i.products.price
        return render(request,'checkout.html',{'cart':cart,'sum':sum})
    def post(self,request):
        cart = Cart.objects.filter(user=request.user)
        user = request.user
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        for item in cart:
            product = item.products
            Orders.objects.create(products=product,user=user,phone=phone,address=address)
            item.delete()
        messages.success(request,'Order placed')
        return redirect('userhome')
dec
def addreview(request,**kwargs):
    review=request.POST.get('rev')
    product_id=kwargs.get('pid')
    product = Products.objects.get(id=product_id)
    user = request.user
    review = Review.objects.create(review=review,user=user,products = product)
    #adding a row
    messages.success(request,"review added")
    return redirect('userhome')
dec
def addtocart(request,pid):
    pro=Products.objects.get(id=pid)
    user=request.user
    Cart.objects.create(products=pro,user=user,status='added')
    return redirect("cart")
@method_decorator(dec,name='dispatch')
class CartlistView(ListView):
    template_name="cart.html"
    queryset=Cart.objects.all()
    context_object_name="cart"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        res = super().get_context_data(**kwargs)
        total = 0
        for i in res['cart']:
            if i.products.is_offer:
                total += i.products.offer_price
            else:
                total += i.products.price
        res['total'] = total
        return res

    def get_queryset(self):
        res=super().get_queryset()
        res=res.filter(user=self.request.user)
        return res
@method_decorator(dec,name='dispatch')       
class CartdeleteView(DeleteView):
    model=Cart
    success_url=reverse_lazy('cart')
    template_name="cartdelete.html"
    pk_url_kwarg="cid"

    
@method_decorator(dec,name='dispatch')
class UserHome(View):
    def get(self,request):
        random_obj = Products.objects.all().order_by('?')[:7]
        return render(request,'userhome.html',{'products':random_obj})
    
# def category(request,category):
#     products = Products.objects.filter(category=category)
#     return render(request,'category_item_list.html',{'products':products})
@method_decorator(dec,name='dispatch')
class Category(ListView):
    template_name='category_item_list.html'
    queryset=Products.objects.all()
    context_object_name='products'
    def get_context_data(self, **kwargs):
        res = Products.objects.filter(category=self.kwargs.get('category')) 
        return {'products':res}
@method_decorator(dec,name='dispatch')   
class DetailView(DetailView):
    template_name='product_details.html'
    queryset=Products.objects.all()
    pk_url_kwarg='pid'
    context_object_name='product'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pid = self.kwargs.get('pid')
        prod = Products.objects.get(id=pid)
        rev = Review.objects.filter(products=prod)
        context["reviews"] = rev 
        return context
    


        
