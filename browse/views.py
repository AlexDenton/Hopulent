from django.shortcuts import render_to_response, get_object_or_404
from browse.models import Beer

def beer(request, beer_id):
	beer = get_object_or_404(Beer, pk=beer_id)
	return render_to_response('browse/beer.html', {'beer': beer})		
