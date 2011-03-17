from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from beer.models import Beer
from brewery.models import Brewery
from style.models import Style


class SearchForm(forms.Form):
	query = forms.CharField(max_length=40)

def search(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			query = form.cleaned_data['query']
			beers = Beer.objects.filter(name__icontains=query)
			breweries = Brewery.objects.filter(name__icontains=query)
			styles = Style.objects.filter(style_name__icontains=query)
			return render_to_response('search/results.html', {'form': form, 'beers': beers, 'breweries': breweries, 'styles': styles}, context_instance=RequestContext(request))
	else:
		form = SearchForm()
		return render_to_response(
			'search/results.html', 
			{'form': form}, 
			context_instance=RequestContext(request)
		)
	
	return render_to_response('search/results.html', {'form': form}, context_instance=RequestContext(request))
