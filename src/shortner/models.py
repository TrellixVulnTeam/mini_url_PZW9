from django.db import models
from .utils import url_generator
from .validator import validate_url
from django.core.urlresolvers import reverse

# Create your models here.
class shorten_url(models.Model):
	url = models.CharField(max_length=220,validators=[validate_url])
	shortcode = models.CharField(max_length=15, unique=True, blank=True)

	def save(self,*args,**kwargs):
		self.shortcode,flag = url_generator(self)
		if flag==1:
			#self.url = validate_url(self.url)
			super(shorten_url,self).save(*args,**kwargs)

	def __str__(self):
		return str(self.url)