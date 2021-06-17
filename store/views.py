from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views import View
from category.models import Category
from cart.views import cart_id
from cart.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


# Create your views here.
class StoreView(View):
	def get(self, request, category_slug=None, *args, **kwargs):
		categories = None
		products = None

		if category_slug !=None:
			categories = get_object_or_404(Category, slug=category_slug)
			products = Product.objects.filter(category=categories, is_available=True)
			paginator = Paginator(products, 2)
			page = request.GET.get('page')
			product_in_page = paginator.get_page(page)
			product_quantity = products.count()
		else:
			products = Product.objects.all().filter(is_available=True)
			paginator = Paginator(products, 2)
			page = request.GET.get('page')
			product_in_page = paginator.get_page(page)
			product_quantity = products.count()

		return render(request, 'store.html', {'products':product_in_page, 'product_quantity':product_quantity})


class ProductDetailView(View):
	def get(self, request, category_slug, product_slug, *args, **kwargs):
		product = Product.objects.get(category__slug=category_slug, slug=product_slug)
		in_cart = CartItem.objects.filter(cart_id__cart_id=cart_id(request), product=product).exists()
		return render(request, 'product_detail.html', {'product':product, 'in_cart':in_cart})

class SearchView(View):
	def get(self, request, *args, **kwargs):
		keyword = request.GET['keyword']
		if keyword:
			products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
			product_quantity = products.count()
		return render(request, 'store.html', {'products':products, 'product_quantity':product_quantity })

























