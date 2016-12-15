from django.contrib import admin

# Register your models here.
from .models import Product
from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","id","price","category","photo"]
	form = ProductForm

	def save_model(self, request, obj, form, change):
		obj.save()

	def get_queryset(self, request):
		qs = super(ProductAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs


admin.site.register(Product,ProductAdmin)