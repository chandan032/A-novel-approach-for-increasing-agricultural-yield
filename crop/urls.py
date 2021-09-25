
from crop import views
from django.urls import path

urlpatterns = [
path("crop",views.crophome,name='crophome'  ),  
path("result/",views.result,name='predictcrop'),

]