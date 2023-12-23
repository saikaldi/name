from django.shortcuts import render
from django.contrib import admin
from django.urls import path,include
# Create your views here.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', include('movie_app.urls'))
]
