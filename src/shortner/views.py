from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse

from .models import shorten_url
from .forms import url_form
from .validator import validate_url
# Create your views here.
def home(request):
	form = url_form()
	context = {
		'form' : form
	}
	if request.method == 'POST':
		#form = url_form(request.POST)
		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			new_url = validate_url(new_url)
			exists = shorten_url.objects.filter(url=new_url).exists()
			if not exists:
				obj = shorten_url.objects.create(url=new_url)
			else:
				obj = shorten_url.objects.filter(url=new_url).first()
			context = {
				'title':'va.com',
				'object':obj,
			}
	return render(request,"shortner/home.html", context)

def index(request,sc=None):
	obj = get_object_or_404(shorten_url,shortcode=sc)
	return HttpResponseRedirect(obj.url)