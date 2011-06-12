from beer.models import Beer 
from brewery.models import Brewery
from style.models import Style
from category.models import Category
from review.models import Review

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django import forms
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

class ReviewForm(forms.Form):
	body = forms.CharField(max_length=1024, widget=forms.Textarea)

@csrf_protect
def beer(request, beer_id):
	beer = get_object_or_404(Beer, pk=beer_id)
	reviews = Review.objects.filter(beer=beer.id)
	rating = reviews.aggregate(Avg('rating'))['rating__avg']

	# Maybe uneccesary	
	if request.user.is_authenticated():
		try:
			user_review = reviews.get(user = request.user)
		except ObjectDoesNotExist:
			user_review = None
	else: user_review = None

	if request.method == 'POST':
		reviewForm = ReviewForm(request.POST)
		if reviewForm.is_valid():
			body = reviewForm.cleaned_data['body']	
			r = Review(review_id=Review.objects.count()+1, user=request.user, beer=beer, body=body)
		        r.save()
			beer.rating = reviews.aggregate(Avg('rating'))['rating__avg']
			beer.save()	
			return render_to_response(
				'beer/beer.html', 
				{'beer': beer, 'rating':rating, 'reviews': reviews, 'user_review': r},
				context_instance=RequestContext(request)
			) 

	else:
		reviewForm = ReviewForm()
		return render_to_response(
			'beer/beer.html', 
			{'beer': beer, 'rating':rating, 'reviews': reviews, 'user_review': user_review, 'reviewForm': reviewForm},
			context_instance=RequestContext(request)
		)

	return render_to_response('beer/beer.html', 
		{'beer': beer, 'rating':rating, 'reviews': reviews, 'user_review': user_review, 'reviewForm': reviewForm},
		context_instance=RequestContext(request)
	)
