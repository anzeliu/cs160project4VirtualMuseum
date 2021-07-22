# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'p4/index.html')

def room(request, room_name):
    return render(request, 'p4/room.html', {
        'room_name': room_name
    })

def home(request, room_name):
    return render(request, 'p4/home.html', {
        'room_name': room_name
    })

def chat_room(request, room_name):
    return render(request, 'p4/chat_room.html', {
        'room_name': room_name
    })

def color_picker(request, room_name):
    return render(request, 'p4/color_picker.html', {
        'room_name': room_name
    })

def drawing_pad(request, room_name):
    return render(request, 'p4/drawing_pad.html', {
        'room_name': room_name
    })

def main_hall(request, room_name):
    return render(request, 'p4/main_hall.html', {
        'room_name': room_name
    })

def museum_display(request, room_name):
    return render(request, 'p4/museum_display.html', {
        'room_name': room_name
    })

def museum_display(request, room_name):
    return render(request, 'p4/museum_display.html', {
        'room_name': room_name
    })

def themed_room_v1(request, room_name):
    return render(request, 'p4/themed_room_v1.html', {
        'room_name': room_name
    })

def themed_room_v2(request, room_name):
    return render(request, 'p4/themed_room_v2.html', {
        'room_name': room_name
    })

def upload_artwork(request, room_name):
    return render(request, 'p4/upload_artwork.html', {
        'room_name': room_name
    })