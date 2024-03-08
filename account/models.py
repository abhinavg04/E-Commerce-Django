from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# product model
class Products(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_images')
    options=(
        ('Vegetables','Vegetables'),
        ('Fruits','Fruits'),
        ('Diary','Diary'),
        ('Spices','Spices'),
    )
    category = models.CharField(max_length=100,choices = options)
    stock = models.IntegerField()
    is_offer = models.BooleanField(default=False,null=True)
    offer_price = models.IntegerField(null=True)
    def __str__(self) -> str:
        return self.title

# cart model
class Cart(models.Model):
    products = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='prod')
    date=models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,default='added')
    def __str__(self) -> str:
        return f'Cart_{self.user}'

# order model
class Orders(models.Model):
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=300)
    options = (
        ('Order Placed','Order Placed'),
        ('Cancelled','Cancelled'),
        ('Shipped','Shipped'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    order_status = models.CharField(max_length=300,default='Order Placed',choices=options)

# review model
class Review(models.Model):
    review = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)