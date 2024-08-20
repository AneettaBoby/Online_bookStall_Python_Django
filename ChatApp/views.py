# chatapp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.http import Http404
from WebApp.models import Register_db
from ChatApp.models import Room,Message


# from .forms import *

# def CreateRoom(request):
#     if request.method == 'POST':
#         try:
#             user = Register_db.objects.get(Username=request.POST['username'])
#             request.session['username'] = user.Username
#         except Register_db.DoesNotExist:
#             request.session['error'] = 'Username not found'
#         room = request.POST['room']
#         try:
#             get_room = Room.objects.get(room_name=room)
#         except Room.DoesNotExist:
#             new_room = Room(room_name=room)
#             new_room.save()
#
#         return redirect('room', room_name=room)
#
#     return render(request, "chat.html")
#
#
# def MessageView(request, room_name,username):
#     get_room = Room.objects.get(room_name=room_name)
#     get_messages = Message.objects.filter(room=get_room)
#
#     context = {
#         "messages": get_messages,
#         "user": username,
#         "room_name": room_name,
#     }
#     return render(request, "_message.html",context)


def MessageView(request):
    get_room = get_object_or_404(Room,room_name="users-chat")
    if request.method == 'POST':
        message = request.POST['message']

        print(message)

        new_message = Message(room=get_room, sender=get_room.Username, message=message)
        new_message.save()

    get_messages = Message.objects.filter(room=get_room)

    context = {
        "messages": get_messages,
    }
    return render(request, "_message.html", context)