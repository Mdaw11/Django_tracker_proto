from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User
from django import forms

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Room(models.Model):
    STATUS = (
        (True, 'Open'),
        (False, 'Closed')
    )
    
    PRIORITIES = (
        ('None', 'None'),
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )
    
    TYPE = (
        ('Misc', 'Misc'),
        ('Bug', 'Bug'),
        ('Help Needed', 'Help Needed'),
        ('Concern', 'Concern'),
        ('Question', 'Question')
    )
    
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='host')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, related_name='topic')
    name = models.CharField(max_length=200)
    assigned = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned', blank=True)
    status = models.BooleanField(choices=STATUS, default=True)
    priority = models.TextField(choices=PRIORITIES, default='None', max_length=10)
    type = models.TextField(choices=TYPE, default='Misc', max_length=15)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]