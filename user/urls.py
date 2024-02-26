from django.urls import path,include
from . views import UserHome
urlpatterns = [
    path('', UserHome.as_view(),name='userhome'),
]