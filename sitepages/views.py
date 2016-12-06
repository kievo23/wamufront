from django.shortcuts import render

# Create your views here.
from product.forms import CheckProduct
def about(request):
	context = {
		'title': "About Us",
		'description':'About Xuwon.com'
	}
	return render(request, "aboutus.html", context)

def contact(request):
	context = {
		'title': "About Us",
		'description':'contact Xuwon.com'
	}
	return render(request, "contact.html", context)

def status(request):
	form  = CheckProduct()
	if request.method == "POST":
		form = CheckProduct(request.POST, request.FILES)
		#if form.is_valid():
	else:
		context = {
			'title': "Check Balance",
			'description':'Check the product that you have reserved and see your balance',
			'form': form
		}
		return render(request, "status.html", context)

def services(request):
	context = {
		'title': "About Us",
		'description':'services Xuwon.com'
	}
	return render(request, "services.html", context)