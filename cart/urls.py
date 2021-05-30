from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, RemoveProductFromCart



urlpatterns = [

path('', CartView.as_view(),name='cart'),
path('<int:pk>/add/', AddToCartView.as_view(), name='add_to_cart'),
path('<int:pk>/remove/', RemoveFromCartView.as_view(), name = 'remove_from_cart'),
path('<int:pk>/remove_product_cart/',RemoveProductFromCart.as_view(), name = 'remove_product_from_cart' ),

]