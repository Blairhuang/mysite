from django.contrib import admin
from .models import Profile

admin.site.register(Profile) #要使得 view profile on admin page(WEBSITE), Register the model in admin file
# 即profile会显示在admin page里面