from django.shortcuts import render, redirect
from Openml.models import Member, Csv, Values 
from django.core.files.storage import FileSystemStorage 
import pdb
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':       
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'index.html')
 
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
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
        return redirect('/upload/csv')
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
    global dataset,X,Y
    if x == 1:
        x=1
    else:
        x=x-1

    y=y-1
    X=dataset.iloc[:,:x].values
    Y=dataset.iloc[:,y:].values
    
def train_test(request):
    global X,Y,X_train, X_test, y_train, y_test
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)
    context = {'msg':'Train and test data got Created'}
    return render(request,'upload_csv.html',context)

def slr(request):
    global X_train,y_train,regressor
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    context = {'slr':'Model prepared for test'}
    return render(request,'upload_csv.html',context)

def prediction(request):
    global X_test,y_pred,regressor
    y_pred = regressor.predict(X_test)    
    context = {'y_pred': y_pred}
    return render(request,'upload_csv.html',context)    

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
    pdb.set_trace()
    plt.scatter(X_test, y_test, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title('Salary vs Experience (Test set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.savefig('Test.png', dpi=220)
    image_data = open("/home/gups/workingdir/ML_using_Django/ML/Test.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")
    