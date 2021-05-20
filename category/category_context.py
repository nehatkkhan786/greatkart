from .models import Category

def CategoryLinks(request):
	categories_links = Category.objects.all()
	return dict(categories_links=categories_links)