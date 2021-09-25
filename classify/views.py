from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage

from fastai import *
from fastai.vision import *
from fastai.metrics import error_rate, accuracy

import numpy as np
import os
# import plant as pl
import json


json_data = open('static/json/remidies.json')
remidies = json.load(json_data)
json_data = open('static/json/categories.json')   
cat_to_name = json.load(json_data)

IMG_WIDTH = 224
IMG_HEIGHT = 224




def index(request):


	return render(request,"index.html")

def predictImage(request):
	print(request.POST.dict())
	fileObj = request.FILES["document"]
	fs=FileSystemStorage()
	filePathName = fs.save(fileObj.name,fileObj)
	filePathName = fs.url(filePathName)

	test_image = "."+filePathName
	# print(test_image)
	print(fileObj)

	

		
		

	IMG = ''
	learn = load_learner(IMG,'static/export_resnet34_model.pkl')
	print(learn.model)

	if fileObj != "":
		img1=open_image(fileObj)
		learn = load_learner(IMG,'static/export_resnet34_model.pkl')
		pred_class,pred_idx,outputs = learn.predict(img1)
		pred=str(pred_class)
		disease = remidies[pred]
		
	# prediction = labels[str(np.argmax(proba[0]))]
	context={
	"filePathName":filePathName,
	"prediction":pred,
	"Remedy" : disease,
	}
	print(context)
	return render(request,"test.html",context)

