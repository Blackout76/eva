from django import forms
from praisal.models import Appraisement

class PraisalForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea, required=True)
	minerals_mode = forms.BooleanField(help_text="Check if you want to estimate minerals component values.", required=False)

class AppraisementForm(forms.Form):
	code = forms.CharField(max_length=8)
	
	def clean_code(self):
		code = self.cleaned_data['code']
		if not Appraisement.objects.filter(code=code).first():
			raise forms.ValidationError("This appraisement does not exist!")
		return code