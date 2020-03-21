from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import cv2
import numpy as np



def img_erosion(saved_image):
	pil_img_obj = Image.open(saved_image.Img).convert('RGB')
	cv_img_obj = np.array(pil_img_obj) 
	
	# Convert RGB to BGR 
	cv_img_obj = cv_img_obj[:, :, ::-1].copy() 

	kernel = cv2.getStructuringElement(saved_image.structural_element, (saved_image.structural_element_size, saved_image.structural_element_size)) 
	#np.ones((saved_image.structural_element_size, saved_image.structural_element_size), np.uint8)
	erosion = cv2.erode(cv_img_obj,kernel,iterations = 1)

	erosion = cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB)
	pil_img_obj = Image.fromarray(erosion)


	f = BytesIO()
	try:
		pil_img_obj.save(f, format='png')
		saved_image.Img.save(saved_image.Img.name, ContentFile(f.getvalue()))

	finally:
		f.close()



def img_dilation(saved_image):
	pil_img_obj = Image.open(saved_image.Img).convert('RGB')
	cv_img_obj = np.array(pil_img_obj) 
	
	# Convert RGB to BGR 
	cv_img_obj = cv_img_obj[:, :, ::-1].copy()

	kernel = cv2.getStructuringElement(saved_image.structural_element, (saved_image.structural_element_size, saved_image.structural_element_size)) 
	#np.ones((saved_image.structural_element_size, saved_image.structural_element_size), np.uint8)
	dilation = cv2.dilate(cv_img_obj,kernel,iterations = 1)

	dilation = cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB)
	pil_img_obj = Image.fromarray(dilation)

	f = BytesIO()
	try:
		pil_img_obj.save(f, format='png')
		saved_image.Img.save(saved_image.Img.name, ContentFile(f.getvalue()))

	finally:
		f.close()
	

def img_opening(saved_image):
	pil_img_obj = Image.open(saved_image.Img).convert('RGB')
	cv_img_obj = np.array(pil_img_obj) 
	
	# Convert RGB to BGR 
	cv_img_obj = cv_img_obj[:, :, ::-1].copy()

	kernel = cv2.getStructuringElement(saved_image.structural_element, (saved_image.structural_element_size, saved_image.structural_element_size)) 
	#np.ones((saved_image.structural_element_size, saved_image.structural_element_size), np.uint8)
	opening = cv2.morphologyEx(cv_img_obj, cv2.MORPH_OPEN, kernel)

	opening = cv2.cvtColor(opening, cv2.COLOR_BGR2RGB)
	pil_img_obj = Image.fromarray(opening)

	f = BytesIO()
	try:
		pil_img_obj.save(f, format='png')
		saved_image.Img.save(saved_image.Img.name, ContentFile(f.getvalue()))

	finally:
		f.close()
	

def img_closing(saved_image):
	pil_img_obj = Image.open(saved_image.Img).convert('RGB')
	cv_img_obj = np.array(pil_img_obj) 
	
	# Convert RGB to BGR 
	cv_img_obj = cv_img_obj[:, :, ::-1].copy()
	
	kernel = cv2.getStructuringElement(saved_image.structural_element, (saved_image.structural_element_size, saved_image.structural_element_size)) 
	#np.ones((saved_image.structural_element_size, saved_image.structural_element_size), np.uint8)
	closing = cv2.morphologyEx(cv_img_obj, cv2.MORPH_CLOSE, kernel)

	closing = cv2.cvtColor(closing, cv2.COLOR_BGR2RGB)
	pil_img_obj = Image.fromarray(closing)

	f = BytesIO()
	try:
		pil_img_obj.save(f, format='png')
		saved_image.Img.save(saved_image.Img.name, ContentFile(f.getvalue()))

	finally:
		f.close()


def img_morphologicalGradient(saved_image):
	pil_img_obj = Image.open(saved_image.Img).convert('RGB')
	cv_img_obj = np.array(pil_img_obj) 
	
	# Convert RGB to BGR 
	cv_img_obj = cv_img_obj[:, :, ::-1].copy()
	
	kernel = cv2.getStructuringElement(saved_image.structural_element, (saved_image.structural_element_size, saved_image.structural_element_size))
	#np.ones((saved_image.structural_element_size, saved_image.structural_element_size), np.uint8)
	gradient = cv2.morphologyEx(cv_img_obj, cv2.MORPH_GRADIENT, kernel)

	gradient = cv2.cvtColor(gradient, cv2.COLOR_BGR2RGB)
	pil_img_obj = Image.fromarray(gradient)

	f = BytesIO()
	try:
		pil_img_obj.save(f, format='png')
		saved_image.Img.save(saved_image.Img.name, ContentFile(f.getvalue()))

	finally:
		f.close()

def img_tophat(saved_image):
	pil_img_obj = Image.open(saved_image.Img).convert('RGB')
	cv_img_obj = np.array(pil_img_obj) 
	
	# Convert RGB to BGR 
	cv_img_obj = cv_img_obj[:, :, ::-1].copy()

	kernel = cv2.getStructuringElement(saved_image.structural_element,(saved_image.structural_element_size, saved_image.structural_element_size))
	#np.ones((saved_image.structural_element_size, saved_image.structural_element_size), np.uint8)
	tophat = cv2.morphologyEx(cv_img_obj, cv2.MORPH_TOPHAT, kernel)

	tophat = cv2.cvtColor(tophat, cv2.COLOR_BGR2RGB)
	pil_img_obj = Image.fromarray(tophat)

	f = BytesIO()
	try:
		pil_img_obj.save(f, format='png')
		saved_image.Img.save(saved_image.Img.name, ContentFile(f.getvalue()))

	finally:
		f.close()



def img_blackhat(saved_image):
	pil_img_obj = Image.open(saved_image.Img).convert('RGB')
	cv_img_obj = np.array(pil_img_obj) 
	
	# Convert RGB to BGR 
	cv_img_obj = cv_img_obj[:, :, ::-1].copy()

	kernel = cv2.getStructuringElement(saved_image.structural_element, (saved_image.structural_element_size, saved_image.structural_element_size)) 
	#np.ones((saved_image.structural_element_size, saved_image.structural_element_size), np.uint8)
	blackhat = cv2.morphologyEx(cv_img_obj, cv2.MORPH_BLACKHAT, kernel)

	blackhat = cv2.cvtColor(blackhat, cv2.COLOR_BGR2RGB)
	pil_img_obj = Image.fromarray(blackhat)

	f = BytesIO()
	try:
		pil_img_obj.save(f, format='png')
		saved_image.Img.save(saved_image.Img.name, ContentFile(f.getvalue()))

	finally:
		f.close()
