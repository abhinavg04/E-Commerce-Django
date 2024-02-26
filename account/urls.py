from django.urls import path,include
from account.views import *
urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('reg', RegView.as_view(),name='reg'),
]
