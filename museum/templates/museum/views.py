# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'p4/index.html')

def home(request):
    return render(request, 'p4/home.html')

def chat_room(request):
    return render(request, 'chat_room.html')

def color_picker(request):
    return render(request, 'color_picker.html')

def drawing_pad(request):
    return render(request, 'drawing_pad.html')

def main_hall(request):
    return render(request, 'main_hall.html')

def museum_display(request):
    return render(request, 'museum_display.html')

def museum_display(request):
    return render(request, 'museum_display.html')

def themed_room_v1(request):
    return render(request, 'themed_room_v1.html')

def themed_room_v2(request):
    return render(request, 'themed_room_v2.html')

def upload_artwork(request):
    return render(request, 'upload_artwork.html')