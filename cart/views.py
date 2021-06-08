from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse

from store.models import Product, Colors, Sizes
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
		color = request.POST.get('color', None)
		size=request.POST.get('size', None)

		product = Product.objects.get(id=pk) #to get the product
		try:
			cart = Cart.objects.get(cart_id=cart_id(request)) #get the cart present in the sessio.
		
		except Cart.DoesNotExist:
			cart = Cart.objects.create(cart_id=cart_id(request))
			cart.save()

		try:
			cart_item = CartItem.objects.get(product=product, cart_id=cart, color=color, size=size)
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

	def post(self, request, pk, *args, **kwargs):
		color = request.POST.get('color', None)
		size=request.POST.get('size', None)

		product = Product.objects.get(id=pk) #to get the product
		try:
			cart = Cart.objects.get(cart_id=cart_id(request)) #get the cart present in the sessio.
		
		except Cart.DoesNotExist:
			cart = Cart.objects.create(cart_id=cart_id(request))
			cart.save()
		try:
			cart_item = CartItem.objects.get(product=product, cart_id=cart, color=color, size=size)
			if cart_item:
				cart_item.quantity += 1 
				cart_item.save()
				return redirect('cart')

		except CartItem.DoesNotExist:
			cart_item = CartItem.objects.create(

				product=product,
				cart_id = cart,
				quantity=1,
				size=Sizes.objects.get(id=size), 
				color=Colors.objects.get(id=color),
				)
			cart_item.save()
			return redirect('cart')


class CartView(View):
	def get(self, request, *args, **kwargs):
		cart_items = {}
		tax = {}
		grand_total = {}
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

def increment_item(request, pk):
	if request.method == 'POST':
		cart_item = CartItem.objects.get(pk=pk)
		print(cart_item)
		cart_item.quantity +=1
		cart_item.save()
		return redirect('cart')
	return redirect('cart')

def decrement_item(request, pk):
	if request.method =='POST':
		cart_item = CartItem.objects.get(pk=pk)
		if cart_item.quantity >1:
			cart_item.quantity -=1
			cart_item.save()
			return redirect('cart')
	return redirect('cart')

def remove_product_from_cart(request, pk):
	cart_item = CartItem.objects.get(pk=pk)
	if cart_item:
		cart_item.delete()
		return redirect('cart')
	return redirect('cart')











