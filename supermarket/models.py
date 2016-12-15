from django.db import models

from django import forms
from django.core.urlresolvers import reverse
from django.utils.six.moves.urllib.parse import (
    quote, quote_plus, unquote, unquote_plus, urlencode as original_urlencode,
    urlparse,
)
from django.contrib.auth.models import User
from userprofile.models import Userprofile
# Create your models here.

class Supermarket(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	description = models.TextField(max_length=1200,blank=False,null=False)
	email = models.EmailField(max_length=255, blank=False, null=False)
	location = models.CharField(max_length=255, blank=False, null=False)
	yourlogo = models.CharField(max_length=255, blank=False, null=False)
	till_no = models.CharField(max_length=255, blank=False, null=False)
	product_counter = models.CharField(max_length=255, blank=False, null=False)
	receipt_counter = models.CharField(max_length=255, blank=False, null=False)
	code = models.CharField(max_length=255, blank=False, null=False)
	receipt_code = models.CharField(max_length=255, blank=False, null=False)
	interest_rate = models.CharField(max_length=255, blank=False, null=False)
	timestamp = models.DateField(auto_now=False, auto_now_add=False)

	def __unicode__(self):
		return self.name