from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

r = DefaultRouter()
r.register('',SellerModelViewSet,basename='seller')
urlpatterns = r.urls
