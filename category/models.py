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

class Category(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)

	def __unicode__(self):
		return self.name
