from django.contrib import admin
from .models import Post #在admin的页面里面加上post

admin.site.register(Post)
# Register your models here. 在admin 的页面里 注册  Register the post created ///这样网页上便可以观察到
