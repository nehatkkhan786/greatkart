from .models import Cart, CartItem
from .views import cart_id

def cart_counter(request):
	cartcounts= 0
	if 'admin' in request.path:
		return{}
	else:
		try:
			cart = Cart.objects.filter(cart_id=cart_id(request))
			cart_items = CartItem.objects.all().filter(cart_id=cart[:1])
			for item in cart_items:
				cartcounts +=item.quantity
		except Cart.DoesNotExist:
			cartcounts = 0
	return dict(cartcounts=cartcounts)

