
# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from browse.models import Beer, Breweries, Categories, Styles

def index(request):
    t = loader.get_template('browse/index.html')
    c = Context({"This is a beer": "This is a beer"})
    return HttpResponse(t.render(c))
def beers(request):
    list_of_beers = Beer.objects.all().order_by('name')
    t = loader.get_template('browse/beers.html')
    c = Context({'list_of_beers': list_of_beers,})
    return HttpResponse(t.render(c))
def brewery(request):
    list_of_breweries = Breweries.objects.all().order_by('name')
    t = loader.get_template('browse/brewery.html')
    c = Context({'list_of_breweries': list_of_breweries,})
    return HttpResponse(t.render(c))
def category(request):
    list_of_categories = Categories.objects.all().order_by('cat_name')
    t = loader.get_template('browse/category.html')
    c = Context({'list_of_categories': list_of_categories,})
    return HttpResponse(t.render(c))
def style(request):
    list_of_styles = Styles.objects.all().order_by('style_name')
    t = loader.get_template('browse/style.html')
    c = Context({'list_of_styles': list_of_styles,})
    return HttpResponse(t.render(c))

#def beer(request, beer_id):
#	beer = get_object_or_404(Beer, pk=beer_id)
#	return render_to_response('browse/beer.html', {'beer': beer})		
