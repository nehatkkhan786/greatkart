from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(blank=True)
	cat_image = models.ImageField(upload_to='photos/category', blank=True)

	class Meta:
		verbose_name='category'
		verbose_name_plural = 'categories'

	def get_category_slug(self):
		return reverse('product_by_category', args=[self.slug])

	def __str__(self):
		return self.category_name 