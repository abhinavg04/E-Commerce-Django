from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from account.models import Products
from .serialzers import Productser
# Create your views here.

class SellerModelViewSet(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=Productser

