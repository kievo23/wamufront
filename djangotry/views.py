from django.contrib.sitemaps import Sitemap
from product.models import Product
import datetime

class PSitemap(Sitemap):
	changefeg = "daily"
	priority = 0.5
	lastmod = datetime.datetime.now()

	def items(self):
		return Product.objects.all()

	