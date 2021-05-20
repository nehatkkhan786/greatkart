from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description = models.TextField(blank=True)
	price = models.FloatField()
	images = models.ImageField(upload_to='photos/products')
	stock = models.IntegerField()
	is_available = models.BooleanField(default=False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def product_url(self):
		return reverse('product_detail', args=[self.category.slug, self.slug])

	def __str__(self):
		return self.product_name