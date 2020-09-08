from django.shortcuts import render, redirect
from Openml.models import Member, Csv
from django.core.files.storage import FileSystemStorage 
import pdb
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    with open('/home/gups/workingdir/ML/Openml/uploaded_file/save.csv', 'wb+') as destination:
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


def reading_csv(f):
    pdb.set_trace()
    dataset = pd.read_csv('/home/gups/workingdir/ML/Openml/uploaded_file/save.csv')



