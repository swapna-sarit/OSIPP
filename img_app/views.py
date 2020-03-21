

from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .models import *

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from . import Morphology



import cv2
import numpy as np


operator_dict = {
			"erosion" :	Morphology.img_erosion, 
			"dilation":	Morphology.img_dilation,
			"opening" :	Morphology.img_opening,
			"closing" :	Morphology.img_closing,
			"morphological gradient" : Morphology.img_morphologicalGradient,
			"tophat"  :	Morphology.img_tophat,
			"blackhat":	Morphology.img_blackhat
		}

#ctr = 0

# Create your views here. 
def uploaded_image_view(request): 
	#global ctr
	#print("\n\n\n*************"+str(ctr)+"*************\n\n\n")
	#ctr = ctr + 1
	saved_image = None
	if request.method == 'POST': 
		
		#print("\n\n\n*************"+str(ctr)+"*************\n\n\n")
		form = ImageByUserForm(request.POST, request.FILES) 

		if form.is_valid(): 
			saved_image = form.save()
			x = operator_dict[saved_image.operation]

			x(saved_image)
			#print("\n\n----------------\n\n123\n\n----------------\n\n")
			return success(request, saved_image)

	else: 
		form = ImageByUserForm()

	print(saved_image) 
	#print("\n\n----------------\n\n456\n\n----------------\n\n")
	return render(request, 'for_image_upload.html', {'form' : form}) 


def success(request, saved_image):
	return render(request, 'for_displaying_image.html', {'Img_disp' : saved_image})


"""


from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .models import *


from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


# Create your views here. 
def uploaded_image_view(request): 

	if request.method == 'POST': 
		form = ImageByUserForm(request.POST, request.FILES) 

		if form.is_valid(): 
			saved_image = form.save() 
			return success(request, saved_image)

	else: 
		form = ImageByUserForm() 
	return render(request, 'for_image_upload.html', {'form' : form}) 


def success(request, saved_image):
	return render(request, 'for_displaying_image.html', {'Img_disp' : saved_image})
 

def fun1(model_instance):
	pil_image_obj = Image.open(model_instance.Img)

"""