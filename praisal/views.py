from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from praisal.models import Appraisement
from .forms.PraisalForm import PraisalForm, AppraisementForm
from .parser import parse
import evepaste

def home(request):
	""" 
	Home view
	"""
	return render(request, 'index.html')

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
		try:
			parsed_content = parse(content)
		except evepaste.Unparsable as ex:
			#if raw_paste:
			#	app.logger.warning("User input invalid data: %s", raw_paste)
			#return render_template('error.html', error='Error when parsing input: ' + str(ex))
			return render(request, 'praisal.html', locals())

		# Appraise content
		appraisal_content = parsed_content

		# Create apparaisement
		new_appraisement = Appraisement(
			parsed_items=parsed_content['results'],
			representative_kind=parsed_content['representative_kind'],
			bad_lines=parsed_content['bad_lines'])
		new_appraisement.save()

		# Redirect
		return redirect('appraisement', code_praisal=new_appraisement.code)
	elif form_view.is_valid():
		code_praisal = form_view.cleaned_data['code']
		appraisement = get_object_or_404(Appraisement, code=code_praisal)
		return redirect('appraisement', code_praisal=appraisement.code)
	else:
		return render(request, 'praisal.html', locals())