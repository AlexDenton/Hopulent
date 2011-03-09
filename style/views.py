from django.shortcuts import render_to_response, get_object_or_404
from style.models import Style

def style(request, style_id):
	style = Style.objects.get(pk=style_id)	
	return render_to_response('style/style.html', {'style': style})
	
