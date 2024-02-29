from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.UserHome.as_view(),name='userhome'),
    path('category/<category>', views.Category.as_view(),name='category'),
    path('product_details/', views.ProductDetails.as_view(),name='product_details'),
]