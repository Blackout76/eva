from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from praisal.models import Appraisement
from .forms.PraisalForm import PraisalForm, AppraisementForm

def appraisement(request, code_praisal):
	""" 
	View to an appraisement
	"""
	appraisement = get_object_or_404(Appraisement, code=code_praisal)
	return render(request, 'appraisement.html', {'appraisement': appraisement})

def praisal(request):
	""" 
	Create an appraisement
	"""
	form_items = PraisalForm(request.POST or None)
	form_view = AppraisementForm(request.POST or None)

	if form_items.is_valid(): 
		content = form_items.cleaned_data['content']
		minerals_mode = form_items.cleaned_data['minerals_mode']

		# Parse content
		parsed_content = content

		# Appraise content
		appraisal_content = parsed_content

		# Create apparaisement
		new_appraisement = Appraisement(content=appraisal_content)
		new_appraisement.save()

		# Redirect
		return redirect('appraisement', code_praisal=new_appraisement.code)
	elif form_view.is_valid():
		code_praisal = form_view.cleaned_data['code']
		appraisement = get_object_or_404(Appraisement, code=code_praisal)
		return redirect('appraisement', code_praisal=appraisement.code)
	else:
		return render(request, 'praisal.html', locals())