from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
        return render_to_response('learn/index.html', context_instance=RequestContext(request))
def beers(request):
        return render_to_response('learn/beers.html', context_instance=RequestContext(request))
def ingredients(request):
        return render_to_response('learn/ingredients.html', context_instance=RequestContext(request))
def glassware(request):
        return render_to_response('learn/glassware.html', context_instance=RequestContext(request))
def rating(request):
        return render_to_response('learn/rating.html', context_instance=RequestContext(request))
