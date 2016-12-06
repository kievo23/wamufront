
from django.template import RequestContext
from django import forms

from .models import Product
from django.forms.extras.widgets import SelectDateWidget
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import delete

class ContactForm(forms.Form):
	BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
	name = forms.CharField(max_length=150)
	email = forms.EmailField()
	#birth_year = forms.DateField(widget=SelectDateWidget())
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'special'}))

class CheckProduct(forms.Form):
	phone = forms.CharField(max_length=12)
	code = forms.CharField(max_length=12)
		
class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['name','price','category','photo','descrip']
		widgets = {'source': forms.HiddenInput()}

	#def clean_photo(self):
		#photo = self.cleaned_data.get('photo')
		#im = get_thumbnail(photo, '100x100', crop='center', quality=99)
		#request.POST['photo'] = im
		#if not 'kev' in jina:
			#raise forms.ValidationError('Should have the name kev')
		#return jina