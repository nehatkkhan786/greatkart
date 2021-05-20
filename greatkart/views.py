from django.shortcuts import  render
from django.views import View
from store.models import Product



class HomePageView(View):
	def get(self, request):
		products = Product.objects.all().filter(is_available=True)
		return render(request, 'home.html', {'products':products})