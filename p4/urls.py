from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('p4/', include('p4.urls')),
    path('p4/home', include('p4.urls')),
    path('p4/main_hall', include('p4.urls')),
    path('p4/themed_room_v1', include('p4.urls')),
    path('p4/themed_room_v2', include('p4.urls')),
    path('p4/upload_artwork', include('p4.urls')),
    path('p4/drawing_pad', include('p4.urls')),
    path('p4/color_picker', include('p4.urls')),
    path('p4/chat_room', include('p4.urls')),
    path('p4/museum_display', include('p4.urls')),
]
