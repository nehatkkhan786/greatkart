from django.urls import path
from .views import CartView, AddToCartView, remove_product_from_cart, increment_item,decrement_item



urlpatterns = [

path('', CartView.as_view(),name='cart'),
path('<int:pk>/add/', AddToCartView.as_view(), name='add_to_cart'),
path('<int:pk>/increment/', increment_item, name='increment_item'),
path('<int:pk>/decrement/', decrement_item, name = 'decrement_item'),
path('<int:pk>/remove_product_from_cart/',remove_product_from_cart, name='remove_product_from_cart' ),

]