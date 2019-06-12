from django.db import models
from django.contrib.auth.models import User 
from PIL import Image
#ADD one to one profile for each user 
#//default user model extend the user model ///创造一对ss一的关系 profile&user

class Profile(models.Model): # inherit from models.model
    user = models.OneToOneField(User, on_delete=models.CASCADE) #USER= 独立用户
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #directory of the uploaded image 上传图片的目标途径

    def __str__(self): # 双重下划线 str method ----print out string  self=instance
        return f'{self.user.username} Profile' 

    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)  #单纯的supersave 会出现 force_insert error


        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size) #resize the image
            img.save(self.image.path) #更改大小的图片 重新覆盖原来的图片

    #def save(self, *args, **kwargs):
        # super.save(*args, **kwargs) 
        # def save(self,*args, **kwargs):
        #   super(Profile, self).save(*args, **kwargs) 





        #self.user.username  最后打印出profile
        #USER PRINT PROFILE---USERNAME--PROFILE
        #change to both database and .... 使用migration//make change overtime 