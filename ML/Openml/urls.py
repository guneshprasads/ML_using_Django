from django.contrib import admin
from django.urls import path,include
from Openml import views

app_name = "Openml"


urlpatterns = [  
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
    path('xy/',views.xy),
    path('missing_values/',views.missing_values),
    path('train_test/',views.train_test),
    path('slr/',views.slr),
    path('Feature_Scaling/',views.Feature_Scaling),
    path('prediction/',views.prediction),
    path('categorical_data/',views.categorical_data),
    path('visual_traindata/',views.visual_traindata),
    path('visual_testdata/',views.visual_testdata),
    path('train_model/',views.train_model,name='train_model'),
]
