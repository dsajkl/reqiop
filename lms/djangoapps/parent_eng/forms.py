from django import forms
#from models import ParentData
from django.forms import ModelForm
from models import P_Data


class Forms(forms.ModelForm):
	class Meta:
		model = P_Data

		#name = forms.CharField(label="Name")
		#email = forms.EmailField(label="Email:")

	#class Meta:
	#	model = ParentData

