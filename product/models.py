from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.utils.six.moves.urllib.parse import (
    quote, quote_plus, unquote, unquote_plus, urlencode as original_urlencode,
    urlparse,
)
from django.contrib.auth.models import User
from userprofile.models import Userprofile
from category.models import Category
# Create your models here.

CATEGORY_CHOICES = (
		('electronics','electronics'),
		('fashion','fashion'),
	)

class Product(models.Model):
	name = models.CharField(max_length=255,blank=False,null=False)
	code = models.CharField(max_length=255,blank=False,null=False)
	price = models.CharField(max_length=255,blank=False,null=False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
	photo = models.FileField(upload_to='uploads/%Y/%m/%d')
	source = models.ForeignKey(User)
	descrip = models.TextField(max_length=1200,blank=False,null=False)
	wamuprice = models.CharField(max_length=255,blank=False,null=True)
	book_amount = models.CharField(max_length=255,blank=False,null=True)
	barcode = models.CharField(max_length=255,blank=False,null=True)
	visible = models.CharField(max_length=255,blank=False,null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	
	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('view', kwargs={'name':quote_plus(self.name),'id':self.id})
