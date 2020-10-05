from django.shortcuts import render, redirect
from Openml.models import Member, Csv, Values 
from django.core.files.storage import FileSystemStorage 
import pdb
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            context = {'sm':'username already exists give another one'}
            return render(request,'index.html',context)
        else:   
            member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
            member.save()
            return redirect('login/')
    else:
        return render(request, 'index.html')
 
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            #member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            pdb.set_trace()
            return redirect('/upload/csv')  
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)  

def handle_uploaded_file(f):
    with open('/home/gups/workingdir/ML_using_Django/ML/Openml/uploaded_file/save.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)       
            
def upload_csv(request):
    if request.method=='POST':
        form = Csv(request.POST,request.FILES)
        f= request.FILES['filename']  
        handle_uploaded_file(f)   
        reading_csv(f)
        context={'msg':'upload done'}           
        return render(request, 'upload_csv.html',context)
    else:
        return render(request, 'upload_csv.html')

dataset = None
def reading_csv(f):
    global dataset
    dataset = pd.read_csv('/home/gups/workingdir/ML_using_Django/ML/Openml/uploaded_file/save.csv')
    

         
def xy(request):
    if request.method == 'GET':
        x = request.GET.get('x')
        y = request.GET.get('y')
        x=int(x)
        y=int(y)
        create_matrix(x,y)        
    context = {'x': x, 'y': y}
    return render(request,'upload_csv.html', context)


def create_matrix(x,y):
    global dataset,X,Y,bx
    if x == 1:
        x=1
    else:
        x=x-1

    y=y-1
    bx=x
    X=dataset.iloc[:,:x].values
    pdb.set_trace()
    Y=dataset.iloc[:,y:].values

def missing_values(request):
    global X
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer.fit(X[:,:])
    X[:,:] = imputer.transform(X[:,:])
    context = {'mv' : 'Done'}
    return render(request,'upload_csv.html',context)

    
def train_test(request):
    global X,Y,X_train, X_test, y_train, y_test
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)
    context = {'tt':'Train and test data got Created'}
    return render(request,'upload_csv.html',context)

def slr(request):
    global X_train,y_train,regressor
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    context = {'slr':'Model prepared for test'}
    return render(request,'train_model.html',context)

def prediction(request):
    global X_test,y_pred,regressor
    y_pred = regressor.predict(X_test)    
    context = {'y_pred': y_pred}
    return render(request,'train_model.html',context)    

def visual_traindata(request):
    global X_train,y_train,regressor
    plt.scatter(X_train, y_train, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title('Salary vs Experience (Training set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.savefig('Train.png', dpi=200)
    image_data = open("/home/gups/workingdir/ML_using_Django/ML/Train.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def visual_testdata(request):
    global X_train,y_train,regressor,X_test, y_test
    plt.scatter(X_test, y_test, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title('Salary vs Experience (Test set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.savefig('Test.png', dpi=220)
    image_data = open("/home/gups/workingdir/ML_using_Django/ML/Test.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def train_model(request):
    return render(request,'train_model.html')

def categorical_data(request):
    global X,dataset,colname,x1,xn
    if request.method == 'GET':
        a = request.GET.get('a')
        qn = int(a)
        qn = qn-2
        colname = dataset.columns[qn]
        x1=dataset[colname]
        xn=x1.nunique()
        ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [qn])], remainder='passthrough')
        pdb.set_trace()
        X = np.array(ct.fit_transform(X))
        pdb.set_trace()
    context = {'a': a}
    return render(request,'upload_csv.html', context)

def Feature_Scaling(request):
    global X_train,X_test,xn
    if request.method == 'GET':
        m = request.GET.get('m')
        n = request.GET.get('n')
        m=int(m)
        n1=int(n)
        m=(m+xn)-3
        n1=(n1+xn-2)+1
        pdb.set_trace()
        sc = StandardScaler()
        X_train[:,m:n1] = sc.fit_transform(X_train[:,m:n1])
        pdb.set_trace()
        X_test[:,m:n1] = sc.transform(X_test[:,m:n1]) 
    context={'msg' : 'Done'}
    return render(request,'train_model.html')
