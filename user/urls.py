from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.UserHome.as_view(),name='userhome'),
    path('category/<category>', views.Category.as_view(),name='category'),
    path('product_details/<int:pid>', views.DetailView.as_view(),name='product_details'),
    path('cart/', views.CartlistView.as_view(),name='cart'),
    path('cart/<int:pid>',views.addtocart,name="addcart"),
    path('deletecart/<cid>',views.CartdeleteView.as_view(),name='cdelt'),
    path('review/<int:pid>',views.addreview,name='arev'),
    path('checkout/',views.Checkout.as_view(),name='checkout'),
    path('order/',views.Order.as_view(),name='order'),
    path('cancelorder/<int:oid>',views.cancelorder,name='cancel'),
    path('review_summary/<int:id>',views.review_summary,name='review_summary')
]