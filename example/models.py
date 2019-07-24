from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Number(models.Model):
    title = models.CharField(max_length=100)
    number = models.TextField()
    number_posted = models.DateTimeField(default=timezone.now)  
    number_author = models.ForeignKey(User,on_delete=models.CASCADE) 
    

