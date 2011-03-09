from django.shortcuts import render_to_response

def index(request):
        return render_to_response('learn/index.html')
def beers(request):
        return render_to_response('learn/beers.html')
def ingredients(request):
        return render_to_response('learn/ingredients.html')
def glassware(request):
        return render_to_response('learn/glassware.html')
def rating(request):
        return render_to_response('learn/rating.html')
