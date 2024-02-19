from django.db import models
from datetime import time

# Create your models here.
class Room(models.Model):
    Name = models.CharField(max_length=200)
    floor_number= models.IntegerField(default=0)
    room_number= models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.Name} at {self.room_number} on {self.floor_number}"
    
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date=models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
    
