from django.shortcuts import render

def home(request):
	""" 
	View home site
	"""
	return render(request, 'index.html')