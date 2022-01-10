from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    #participants = 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Activity, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[0:50]