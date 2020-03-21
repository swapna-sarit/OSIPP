from django.db import models
import cv2

# Create your models here.

# models.py 

STRUCTURAL_ELEMENT_CHOICES = [
    (cv2.MORPH_RECT, 'Rectangle'),
    (cv2.MORPH_ELLIPSE, 'Ellipse'),
    (cv2.MORPH_CROSS, 'Cross'),
]

OPERATION_CHOICES = [
    ("erosion", 'Erosion'),
    ("dilation", 'Dilation'),
    ("opening", 'Opening'),
    ("closing", 'Closing'),
    ("morphological gradient", 'Morphological Gradient'),
    ("tophat", 'Tophat'),
    ("blackhat", 'Blackhat'),
]



class ImageByUser(models.Model): 
	name = models.CharField(max_length=50) 
	Img = models.ImageField(upload_to='images/')
	operation = models.CharField(max_length=50, choices = OPERATION_CHOICES, default = "erosion")
	structural_element = models.IntegerField(choices = STRUCTURAL_ELEMENT_CHOICES, default = cv2.MORPH_RECT)
	structural_element_size = models.IntegerField(default = 5) 
