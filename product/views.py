from django.shortcuts import render
from django.template.defaultfilters import stringfilter
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from urllib import unquote
from endless_pagination.decorators import page_template
from haystack.generic_views import SearchView
from haystack.forms import ModelSearchForm, HighlightedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

from .forms import ProductForm, ContactForm
from .models import Product
from category.models import Category
from userprofile.models import Userprofile

# Create your views here.

def contact(request):
	form = ContactForm()
	context = {
		'form' : form,
		'title' : 'Contact Us'
	}
	return render(request, 'contact.html',context)

def productEdit(request,id):
	try:
		record = Product.objects.get(id=id)
	except Product.DoesNotExist:
		raise Http404("Question does not exist")
	form = ProductForm(instance= record)
	context= {
		'title':'',
		'form' :form
	}
	return render(request, 'edit.html', context)

def productView(request,name,id):
	try:
		record = Product.objects.get(id=id)
		user = User.objects.get(id=int(record.source.id))
		userprofile = user.userprofile
	except Product.DoesNotExist:
		raise Http404("Record does not exist")
	context= {
		'title':record.name,
		'record' :record,
		'user':user,
		'userprofile':userprofile
	}
	return render(request, 'view.html', context)

#@page_template('load_chunks.html')
def products(request, template='products.html', page_template='products_template.html'):
	records = list(Product.objects.all())
	categories = Category.objects.all()
	context= {
		'title':'Inventory',
		'records' : records,
		'categories' : categories
	}
	if request.is_ajax():
		template = page_template
	return render_to_response(template, context, context_instance=RequestContext(request))



def search(request, template='search_template.html', page_template='search_template_chunk.html'):
	query = request.GET['q']
	categories = Category.objects.all()
	products = SearchQuerySet().models(Product).filter(text = query)
	context = {
		'records' : products,
		'title' : 'Search products',
		'categories' : categories
	}
	if request.is_ajax():
		template = page_template
	#return render(request, 'search_template.html',context)
	return render_to_response(template, context, context_instance=RequestContext(request))


def home(request):
	form = ProductForm(request.POST or None)
	context = {
		'form':form,
		'title': 'The First App'
	}
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			context = {
				'title': 'Thanks man'
			}
	
	return render(request, 'home.html', context)
