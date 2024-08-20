import shortuuid
from django.db import models

from WebApp.models import Register_db


# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.ForeignKey(Register_db,on_delete=models.CASCADE)
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.sender.Username} : {self.message}'








