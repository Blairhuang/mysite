from django.db.models.signals import post_save 
from django.contrib.auth.models import User # post_save signal---sender 信号发送者
from django.dispatch import receiver 
from .models import Profile  #want the user profile created for each new user     
#，signals（信号）允许若干 senders（寄件人）通知一组 receivers（接收者）

#CREATE PROFILE
@receiver(post_save,sender=User) #DECORATORS receiver为装饰器 arguments 包括 post_save=signal发送的信号，和发送者 User
def creat_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) #CREATE user ...decorator装饰器的作用是给函数增强功能 增加动态功能

#SAVE PROFILE
@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):  
    instance.profile.save()

#If user save, send the signal, and creat_profile 接受
