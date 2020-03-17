from django.urls import path

from api import views

urlpatterns = [

    path('albums/', views.Album.as_view()),
    path('photos/', views.Photo.as_view()),
]
