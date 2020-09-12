from django.db import models
from django import forms
from django.forms import ModelForm


# Create your models here.  
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
 
    def __str__(self):
        return self.firstname + " " + self.lastname
  
  
    class Meta:  
        db_table = "web_member"

class Csv(forms.Form):
	title = forms.CharField(max_length=50)
	myfile = forms.FileField()

class Values(models.Model):
    x_value=models.CharField(max_length=7)
    y_value=models.CharField(max_length=7)

