from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
import pickle

def salaryML(request):
    if(request.method =='GET'):
        return render(request,'index.html')
    else:
        data = request.POST['value']
        model = pickle.load(open('salary.pkl','rb'))
        ans = model.predict([[data]])
        ans = list(ans)
        if(ans[0]<0 and ans[0]<50): ans[0] = 0
        return render(request,'index.html',{'ans':str(ans[0])})

