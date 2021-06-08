from django.db import models
from store.models import Product, Colors, Sizes

# Create your models here.
class Cart(models.Model):
	cart_id = models.CharField(max_length=250)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.cart_id


class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete= models.CASCADE)
	cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	color = models.ForeignKey(Colors, on_delete= models.CASCADE, blank=True, null=True)
	size = models.ForeignKey(Sizes, on_delete=models.CASCADE,null=True, blank=True, related_name='cart_item_size')
	is_active = models.BooleanField(default=True)

	def subtotal(self):
		return self.product.price * self.quantity

	def __str__(self):
		return self.product.product_name


