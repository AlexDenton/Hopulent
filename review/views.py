from django.shortcuts import render_to_response, get_object_or_404
from beer.models import Beer

def review(request, beer_id):
	beer = Beer.get_object_or_404(pk=beer_id)
	return render_to_response('review/review.html', {'beer': beer})
	
