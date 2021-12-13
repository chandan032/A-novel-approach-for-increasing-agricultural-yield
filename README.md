# A-novel-approach-for-increasing-agricultural-yield
 A web application serving two functionalities of plant disease detection and crop prediction

## Official implementation of A novel approach for increasing agricultural yield
[Click here to go to research paper](https://indjst.org/articles/an-artificial-intelligence-based-approach-for-increasing-agricultural-yield)

## Link to project
[click here to see the project](https://crop-plant.herokuapp.com/)


## About
India being an agriculture-dependent community relies primarily on agriculture for its economy. Enhancing the agriculture sector thus becomes the most critical challenge for our country's economy. This paper offers a better approach to increasing agricultural production by integrating the latest developments in technology into agriculture. The two biggest issues the farmers face is 1. Knowing which crop to be sown under different conditions 2. To grasp the plant diseases and to predict them. This paper addresses these two issues by predicting a suitable crop based on certain parameters, and secondly, by detecting the diseases in the plant from a leaf picture.

Crop prediction works by taking certain parameters such as temperature, humidity, soil moisture, rainfall, and pH into consideration and predicting the best crop to grow under those considerations. This paper proposes two methods: Logistic Regression (LR) and Support Vector Machine (SVM) with an accuracy of 93% and 97% respectively and can predict the class of 13 crops.


Detection of plant disease takes a picture of the plant leaf as an input, and if any, identifies diseases present in the plant. This research uses an open dataset of 54,306 photos of healthy and diseased crops and predicts diseases in 38 different categories from 14 specific crops. The system uses Convolution Neural Network (CNN)with ResNet152 architecture to predict plant disease and the accuracy achieved was 96%.

## Local Installation steps
pip install -r requirements.txt <br>
Navigate to prject folder <br>
python manage.py runserver <br>

## Please visit the research link for more details
