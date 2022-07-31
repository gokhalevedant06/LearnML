from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
import pickle

def Model(request):
    if(request.method =='GET'):
        return render(request,'index.html')
    else:
        region = request.POST['region']
        print(region)
        numberOfDeliveries = request.POST['deliveries']
        print(numberOfDeliveries)
        truckAge = request.POST['truckAge']
        print(truckAge)
        model = pickle.load(open('deliveries.pkl','rb'))
        ans = model.predict([[region,numberOfDeliveries,truckAge]])
        print(ans)
        ans = list(ans)
        return render(request,'index.html',{'ans':str(ans[0])})
