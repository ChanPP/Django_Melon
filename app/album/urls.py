from django.urls import path

from album import views

app_name = 'album'
urlpatterns = [
    path('', views.album_list, name='album-list'),
]
