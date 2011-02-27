from django.shortcuts import render_to_response, get_object_or_404

from beer.models import Beer 
from brewery.models import Brewery
from style.models import Style
from category.models import Category

def beer(request, beer_id):
	beer = get_object_or_404(Beer, pk=beer_id)
	brewery = Brewery.objects.get(pk=beer.brewery_id)
	style = Style.objects.get(pk=beer.style_id)
	cat = Category.objects.get(pk=beer.cat_id)
	return render_to_response('beer/beer.html', {'beer': beer, 'brewery': brewery, 'style': style, 'cat': cat})	
