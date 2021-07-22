from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.indexP4, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('home', views.home, name='home'),
    path('main_hall', views.main_hall, name='main_hall'),
    path('themed_room_v1', views.themed_room_v1, name='themed_room_v1'),
    path('themed_room_v2', views.themed_room_v2, name='themed_room_v2'),
    path('upload_artwork', views.upload_artwork, name='upload_artwork'),
    path('drawing_pad', views.drawing_pad, name='drawing_pad'),
    path('color_picker', views.color_picker, name='color_picker'),
    path('chat_room', views.chat_room, name='chat_room'),
    path('museum_display', views.museum_display, name='museum_display'),
]
