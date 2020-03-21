from django.urls import path
from . import views

urlpatterns = [
	path('', views.uploaded_image_view, name = 'uploaded-img-stuff'),
	path('success', views.success, name = 'success')
]

