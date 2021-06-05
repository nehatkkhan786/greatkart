from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse

from store.models import Product
from .models import CartItem, Cart
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def cart_id(request):
	cart = request.session.session_key
	if not cart:
		cart = request.session.create()
	return cart

class AddToCartView(View):
	def get(self, request, pk, *args, **kwargs):
		product = Product.objects.get(id=pk) #to get the product

		try:
			cart = Cart.objects.get(cart_id=cart_id(request)) #get the cart present in the sessio.
		
		except Cart.DoesNotExist:
			cart = Cart.objects.create(cart_id=cart_id(request))
			cart.save()

		try:
			cart_item = CartItem.objects.get(product=product, cart_id=cart)
			cart_item.quantity += 1
			cart_item.save()
			return redirect('cart')

		except CartItem.DoesNotExist:
			cart_item = CartItem.objects.create(

				product=product,
				cart_id = cart,
				quantity=1,

				)
			cart_item.save()
			return redirect('cart')

class RemoveFromCartView(View):
	def get(self, request, pk, *args, **kwargs):
		cart = Cart.objects.get(cart_id =cart_id(request))
		product = Product.objects.get(id=pk)
		cart_item = CartItem.objects.get(product=product, cart_id=cart)
		if cart_item.quantity > 1:
			cart_item.quantity -= 1
			cart_item.save()
		else:
			cart_item.delete()
		return redirect('cart')

class RemoveProductFromCart(View):
	def get(self, request, pk, *args, **kwargs):
		cart = Cart.objects.get(cart_id=cart_id(request))
		product = get_object_or_404(Product, pk=pk)
		cart_item = CartItem.objects.get(product=product, cart_id=cart)
		cart_item.delete()
		return redirect('cart')


class CartView(View):
	def get(self, request, *args, **kwargs):
		try:
			total = 0 
			cart= Cart.objects.get(cart_id=cart_id(request))
			cart_items = CartItem.objects.filter(cart_id=cart, is_active=True)

			for cart_item in cart_items:
				total = total + cart_item.product.price * cart_item .quantity
			tax = (18 * total)/100
			grand_total = tax + total

		except ObjectDoesNotExist:
			pass
		return render(request, 'cart.html', {'cart_items':cart_items,'total':total, 'tax':tax,'grand_total':grand_total})















