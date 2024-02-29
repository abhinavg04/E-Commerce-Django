from django.urls import path,include
from account.views import *
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('reg/', RegView.as_view(),name='reg'),
    path('logout/',logout_user,name='logout'),
    path('user-page/',user_page,name='user_page'),
    path('update_user/',update_user,name='update_user'),
    path('update_password/',UpdatePassword.as_view(),name='update_password'),
]
