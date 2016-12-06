import datetime
from haystack import indexes
from .models import Product

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	pub_date = indexes.DateTimeField(model_attr='timestamp')
	content_auto = indexes.EdgeNgramField(model_attr = 'name')
	category = indexes.EdgeNgramField(model_attr = 'category')

	def get_model(self):
		return Product
	def index_queryset(self, using=None):
		return self.get_model().objects.all()

