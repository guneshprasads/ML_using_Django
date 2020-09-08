from django.contrib import admin
from django.urls import path,include
from Openml import views

app_name = "Openml"


urlpatterns = [  
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    #path('up/',views.up,name='up'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
]