from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views import View
from category.models import Category




# Create your views here.
class StoreView(View):
	def get(self, request, category_slug=None, *args, **kwargs):
		categories = None
		products = None

		if category_slug !=None:
			categories = get_object_or_404(Category, slug=category_slug)
			products = Product.objects.filter(category=categories, is_available=True)
			product_quantity = products.count()
		else:

			products = Product.objects.all().filter(is_available=True)
			product_quantity = products.count()

		return render(request, 'store.html', {'products':products, 'product_quantity':product_quantity})


class ProductDetailView(View):
	def get(self, request, category_slug, product_slug, *args, **kwargs):
		product = Product.objects.get(category__slug=category_slug, slug=product_slug)
		return render(request, 'product_detail.html', {'product':product})