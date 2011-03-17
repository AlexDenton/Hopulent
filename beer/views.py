from beer.models import Beer 
from brewery.models import Brewery
from style.models import Style
from category.models import Category
from review.models import Review

from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django import forms
from django.template import RequestContext

class ReviewForm(forms.Form):
	title = forms.CharField(max_length=40)
	body = forms.CharField(max_length=1024, widget=forms.Textarea)
	

def beer(request, beer_id):
	beer = get_object_or_404(Beer, pk=beer_id)
	reviews = Review.objects.filter(beer=beer.id)
	rating = reviews.aggregate(Avg('rating'))
	brewery = Brewery.objects.get(pk=beer.brewery_id)
	
	if request.user.is_authenticated():
		user_review = Review.objects.get(user = request.user)
	else: user_review = None
	
	try:
		style = Style.objects.get(pk=beer.style_id)	
	except ObjectDoesNotExist:
		style = None
		
	if request.method == 'POST':
		reviewForm = ReviewForm(request.POST)
		if reviewForm.is_valid():
			title = reviewForm.cleaned_data['title']
			body = reviewForm.cleaned_data['body']	
			r = Review(review_id=Review.objects.len()+1, user=request.user, beer=beer, title=title, body=body)
			return render_to_response(
				'beer/beer.html', 
				{'beer': beer, 'brewery': brewery, 'style': style, 'reviews': reviews, 'rating': rating, 'user_review': user_review, 'reviewForm': reviewForm},
				context_instance=RequestContext(request)
			)
	
	else:
		reviewForm = ReviewForm()
		return render_to_response(
			'beer/beer.html', 
			{'beer': beer, 'brewery': brewery, 'style': style, 'reviews': reviews, 'rating': rating, 'user_review': user_review, 'reviewForm': reviewForm},
			context_instance=RequestContext(request)
		)
		
	return render_to_response('beer/beer.html', 
		{'beer': beer, 'brewery': brewery, 'style': style, 'reviews': reviews, 'rating': rating, 'user_review': user_review, 'reviewForm': reviewForm},
		context_instance=RequestContext(request)
	)
