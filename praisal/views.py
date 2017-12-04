from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from praisal.models import Appraisement

def home(request):
	text = """<h1>Welcome on praisal</h1>"""
	return HttpResponse(text)

def view_praisal(request, code_praisal):
	""" 
	View that draw an appraisement
	"""
	appraisement = get_object_or_404(Appraisement, code=code_praisal)
	return render(request, 'appraisement.html', {'appraisement': appraisement})
