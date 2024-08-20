from django.urls import path,include
from ChatApp import views
# urlpatterns = [
#     path('create-room/', views.CreateRoom, name='create-room'),
#     path('room/<str:room_name>/<str:username>/', views.MessageView, name='room'),
# ]


urlpatterns = [
    path('chatview/',views.MessageView,name="chatview"),
    # path('chat/room/<str:room_name>', views.MessageView, name="chatroom"),
]