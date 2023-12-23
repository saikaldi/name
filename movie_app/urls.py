from django.urls import path
from . import views

urlpatterns = [
    path('', views.directors_view),
    path('<int:id>/', views.director_detail_api_view),

    path('', views.movie_list_view),
    path('<int:id>/', views.movie_detail_api_view),

    ]