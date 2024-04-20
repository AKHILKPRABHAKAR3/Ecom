from django.urls import path
from store import views
urlpatterns=[
    path('home/',views.Home.as_view(),name='home'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.Logout.as_view(),name='logout'),
    # path('collection/',views.Collections.as_view(),name='collection')
    path('products/<int:id>/',views.products.as_view(),name='products'),
    path('productdetails/<int:id>',views.product_details.as_view(),name='p_details'),
    path('cart/<int:pk>/',views.Addcartview.as_view(),name='cart'),
    path('deletecart/<int:pk>/',views.Delete_cart.as_view(),name='cartdelete'),
    path('cartdetails/',views.Cartdetailview.as_view(),name='cartdetails'),
    path('order/<int:id>',views.OrderView.as_view(),name='order'),
    path('orderlist/',views.OrderList.as_view(),name='orderlist'),
    path('orderdelete/<int:id>/',views.Order_Delete.as_view(),name='orderdelete'),
    path("search/all",views.Searchview.as_view(),name="srch")

    
    
]