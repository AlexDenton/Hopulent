from django.shortcuts import render_to_response, get_object_or_404
from beer.models import Beer
from django import forms

class ReviewForm(forms.Form):
        title = forms.CharField(max_length=40)
        body = forms.CharField(max_length=1024, widget=forms.Textarea)

def review(request):
	if request.method == 'POST':
		reviewForm = ReviewForm(request.POST)
		if reviewForm.is_valid():
			body = reviewForm.cleaned_data['body']	
			r = Review(review_id=Review.objects.len()+1, user=request.user, beer=beer, body=body)
			return render_to_response(
				'beer/beer.html', 
				{'reviewForm': reviewForm},
				context_instance=RequestContext(request)
			)

	else:
		reviewForm = ReviewForm()
		return render_to_response(
			'beer/beer.html', 
			{'reviewForm': reviewForm},
			context_instance=RequestContext(request)
		)

	return render_to_response('beer/beer.html', 
		{'reviewForm': reviewForm},
		context_instance=RequestContext(request)
	)	
