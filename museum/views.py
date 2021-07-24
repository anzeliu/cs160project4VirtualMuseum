# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'museum/index.html')

def home(request):
    return render(request, 'museum/home.html')

def chat_room(request):
    return render(request, 'museum/chat_room.html')

def color_picker(request):
    return render(request, 'museum/color_picker.html')

def drawing_pad(request):
    return render(request, 'museum/drawing_pad.html')

def drawing_pad_v2(request):
    return render(request, 'museum/drawing_pad_v2.html')

def main_hall(request):
    return render(request, 'museum/main_hall.html')

def museum_display(request):
    return render(request, 'museum/museum_display.html')

def museum_display_v2(request):
    return render(request, 'museum/museum_display_v2.html')

def themed_room_v1(request):
    return render(request, 'museum/themed_room_v1.html')

def themed_room_v1_v2(request):
    return render(request, 'museum/themed_room_v1_v2.html')

def themed_room_v2(request):
    return render(request, 'museum/themed_room_v2.html')

def upload_artwork(request):
    return render(request, 'museum/upload_artwork.html')

def upload_artwork_v2(request):
    return render(request, 'museum/upload_artwork_v2.html')

def save_artwork(request):
    return render(request, 'museum/save_artwork.html')

def save_artwork_v2(request):
    return render(request, 'museum/save_artwork_v2.html')

def save_artwork_new(request):
    return render(request, 'museum/save_artwork_new.html')

def save_artwork_new_v2(request):
    return render(request, 'museum/save_artwork_new_v2.html')

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })
