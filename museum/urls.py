from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('main_hall', views.main_hall, name='main_hall'),
    path('themed_room_v1', views.themed_room_v1, name='themed_room_v1'),
    path('themed_room_v1_v2', views.themed_room_v1_v2, name='themed_room_v1_v2'),
    path('themed_room_v2', views.themed_room_v2, name='themed_room_v2'),
    path('upload_artwork', views.upload_artwork, name='upload_artwork'),
    path('upload_artwork_v2', views.upload_artwork_v2, name='upload_artwork_v2'),
    path('drawing_pad', views.drawing_pad, name='drawing_pad'),
    path('drawing_pad_v2', views.drawing_pad_v2, name='drawing_pad_v2'),
    path('color_picker', views.color_picker, name='color_picker'),
    path('chat_room', views.chat_room, name='chat_room'),
    path('museum_display', views.museum_display, name='museum_display'),
    path('museum_display_v2', views.museum_display_v2, name='museum_display_v2'),
    path('save_artwork', views.save_artwork, name='save_artwork'),
    path('save_artwork_v2', views.save_artwork_v2, name='save_artwork_v2'),
    path('save_artwork_new', views.save_artwork_new, name='save_artwork_new'),
    path('save_artwork_new_v2', views.save_artwork_new_v2, name='save_artwork_new_v2'),
    path('<str:room_name>/', views.room, name='room')
]
