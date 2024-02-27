from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.UserHome.as_view(),name='userhome'),
    path('category/<category>', views.category,name='category'),
]