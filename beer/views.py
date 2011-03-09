from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg

from beer.models import Beer 
from brewery.models import Brewery
from style.models import Style
from category.models import Category
from review.models import Review

def beer(request, beer_id):
	beer = get_object_or_404(Beer, pk=beer_id)
	rating = Review.objects.filter(beer_id=beer_id).aggregate(Avg('rating'))
	try:
		brewery = Brewery.objects.get(pk=beer.brewery_id)
		style = Style.objects.get(pk=beer.style_id)
		cat = Category.objects.get(pk=beer.cat_id)
		return render_to_response('beer/beer.html', {'beer': beer, 'brewery': brewery, 'style': style, 'cat': cat, 'rating': rating})	
	except ObjectDoesNotExist:
		return render_to_response('beer/beer.html', {'beer': beer, 'brewery': brewery, 'rating': rating})
		
