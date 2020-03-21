# forms.py 
from django import forms 
from .models import *

class ImageByUserForm(forms.ModelForm):
	class Meta:
		model = ImageByUser
		fields = ['name', 'Img', 'operation', 'structural_element', 'structural_element_size'] 
