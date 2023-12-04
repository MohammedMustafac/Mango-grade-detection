from django.shortcuts import render
import pandas as pd
import sklearn 
from sklearn import tree
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
def mango(request):
     if(request.method=="POST"):
        data=request.POST
        weight=data.get('weight')
        length=data.get('length')
        circumference=data.get('circumference')
        path="C:\\Users\\91782\\OneDrive\\Desktop\\mango\\Data.csv"
        data1=pd.read_csv(path)
        inputs=data1.drop(['No','Grade'],'columns')
        outputs=data1.drop(['No','Weight','Length','Circumference'],'columns')
        x_train,x_test,y_train,y_test=train_test_split(inputs,outputs,train_size=0.8)
        model=SVC()
        model.fit(x_train,y_train)
        info=model.predict([[weight,length,circumference]])
        return render(request,"mango.html",context={'info':info})

     return render(request,'mango.html')

# Create your views here.
