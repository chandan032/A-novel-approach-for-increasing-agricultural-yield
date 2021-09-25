
from . import views
from django.urls import path

urlpatterns = [path("plant",views.index,name='planthome'),
path("predict",views.predictImage,name='predictImage')]