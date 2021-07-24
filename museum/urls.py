from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('main_hall', views.main_hall, name='main_hall'),
    path('themed_room_v1', views.themed_room_v1, name='themed_room_v1'),
    path('themed_room_v2', views.themed_room_v2, name='themed_room_v2'),
    path('themed_room_v2_variant', views.themed_room_v2_variant, name='themed_room_v2_variant'),
    path('upload_artwork', views.upload_artwork, name='upload_artwork'),
    path('drawing_pad', views.drawing_pad, name='drawing_pad'),
    path('color_picker', views.color_picker, name='color_picker'),
    path('chat_room', views.chat_room, name='chat_room'),
    path('museum_display', views.museum_display, name='museum_display'),
    path('save_artwork', views.save_artwork, name='save_artwork'),
    path('save_artwork_new', views.save_artwork_new, name='save_artwork_new'), 
    path('<str:room_name>/', views.room, name='room')
]
