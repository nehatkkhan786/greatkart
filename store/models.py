from django.db import models
from category.models import Category
from django.urls import reverse
from multiselectfield import MultiSelectField


# Create your models here.


class Colors(models.Model):
	color_name = models.CharField(max_length=200)

	def __str__(self):
		return self.color_name

class Sizes(models.Model):
	size = models.CharField(max_length=200)

	def __str__(self):
		return self.size





class Product(models.Model):
	product_name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description = models.TextField(blank=True)
	price = models.FloatField()
	images = models.ImageField(upload_to='photos/products')
	stock = models.IntegerField()
	sizes = models.ManyToManyField(Sizes, blank=True)
	colors = models.ManyToManyField(Colors)
	is_available = models.BooleanField(default=False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def product_url(self):
		return reverse('product_detail', args=[self.category.slug, self.slug])

	def __str__(self):
		return self.product_name