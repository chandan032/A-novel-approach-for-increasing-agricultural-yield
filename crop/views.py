from django.shortcuts import render, redirect
import pickle
import numpy as np

# Create your views here.
def home(request):
    return render(request,"home.html")

def crophome(request):
    return render(request,"crophome.html")

def getPredictions(final_features):
    import pickle
    model_svm = pickle.load(open('cropsvm.sav', "rb"))
    pred_svm = model_svm.predict(final_features)
    cropsvm ,fertilizer_svm = get_fertilizer(pred_svm)
    model_lr = pickle.load(open("croplr.sav", "rb"))
    pred_lr = model_lr.predict(final_features)
    croplr, fertilizer_lr = get_fertilizer(pred_lr)
    context={
	"cropsvm":cropsvm,
	"fertilizer_svm":fertilizer_svm,
	"croplr" : croplr,
    "fertilizer_lr" : fertilizer_lr
	}
    print(context)
    return context


def get_fertilizer(pred):
    g = pred[0]
    Fertilizer=""

    if g==0:
        f="NO"
        
    if g==1:
        f = "Wheat"
        Fertilizer="Super phosphate-155 kg/acre \n Muriate of potash-20 kg/acre \n Nitro phophate-125 kg/acre"

    if g==2:
        f = "Oats"
        Fertilizer="Nitorgen-110 kg/acre \n P2O5 20-30 kg/acre \n K2O-17 kg/acre \n Sulphur-10 kg/acre\n"

    if g==3:
        f = "Gram"
        Fertilizer="Nitorgen-12.5 kg/acre  \nP2O5-25 kg/acre \nK2O-12.5 kg/acre \nSulphur-10 kg/acre \n"

    if g==4:
        f = "Pea"
        Fertilizer="Nitorgen-55 kg/acre \nPhosphorus-20 kg/acre \nPotash-40 kg/acre \n"

    if g==5:
        f = "Tea"
        Fertilizer="Ammonium phosphate-35 kg/acre \nPotassium sulphate-15 kg/acre \nMOP-12 kg/acre \nMagnesium sulphate-15 kg/acre \nZinc sulphate-3 kg/acre \n"

    if g==6:
        f = "Rice"
        Fertilizer="P2O5-35 kg/acre \nK2O-50 kg/acre \n"

    if g==7:
        f = "Bajra"
        Fertilizer="Nitrogen-80 kg/acre \nPhosphorous-40 kg/acre \nPhotash-40 kg/acre \n"

    if g==8:
        f = "Maize"
        Fertilizer="P2O5-24 kg/acre \nK2O-12 kg/acre \n"

    if g==9:
        f = "Potato"
        Fertilizer="Nitrogen-150 kg/acre \nPhosphorous-60 kg/acre \nPotassium-90 kg/acre \n"

    if g==10:
        f = "Groundnut"
        Fertilizer="Nitrogen-25 kg/acre \nPhosphorous-50 kg/acre \nPotassium-75 kg/acre \nSulphur sludge-60 kg/acre \n"

    if g==11:
        f = "Jute"
        Fertilizer="Urea-8 kg/acre \nNitrogen-10 kg/acre \nN,P2O5 and K2O-20 kg/acre \n"

    if g==12:
        f = "Sugarcane"
        Fertilizer="Zinc sulphate-37.5 kg/acre \nFerrous sulphate-100 kg/acre \n"

    if g==13:
        f = "Turmeric"
        Fertilizer="Nitrogen-120 kg/acre \nP2O5-50 kg/acre \nK2O-80 kg/acre \n"

    if g==14:
        f = "No Crop"  
    return f,Fertilizer

        

# our result page view
def result(request):
    login_data = request.POST.dict()
    Temperature = int(login_data.get('Temperature'))
    Humidity = int(login_data.get('Humidity'))
    Soil_Moisture = int(login_data.get('Soil_Moisture'))
    Rainfall = int(login_data.get('Rainfall'))
    PH = int(login_data.get('PH'))
    final_features = [Temperature,Humidity,Soil_Moisture,Rainfall,PH]
    #x=np.asarray(final_features).reshape(1,-1)
    x = [np.array(final_features)]

    context = getPredictions(x)
    print(context)

    return render(request, 'result.html', context)
