import os
from PIL import Image

from django.db import models
from django.contrib.auth.models import AbstractUser
from custom_login.myusermanager import MyUserManager

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}{ext}"
    # final_name = f"{instance.id}-{instance.title}{ext}"
    return f"profile/{final_name}"




class MyUser(AbstractUser):
    username = None
    mobile = models.CharField(max_length=11, unique=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    profile_name= models.CharField(max_length=20, blank=True,null=True)
    profile_pic=models.ImageField(upload_to=upload_image_path,default='site/unnamed.png', null=True, blank=True, verbose_name='تصویر پروفایل')
    profile_bio = models.TextField(verbose_name='بیوگرافی', null=True, blank=True)
    is_block = models.BooleanField(default=False, verbose_name='بلاک بودن')




    objects = MyUserManager()

    USERNAME_FIELD = 'mobile'

    REQUIRED_FIELDS = []

    backend = 'custom_login.mybackend.ModelBackend'

    
    
        
    def __str__(self):
        return str(self.profile_name)
    
    
    




    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_pic.path)
        width, height = img.size  # Get dimensions
        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))
            width, height = img.size

            # check which one is smaller
            if height < width:
                # make square by cutting off equal amounts left and right
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img = img.crop((left, top, right, bottom))
                img.thumbnail((300, 300))
                img.save(self.profile_pic.path)

            elif width < height:
                # make square by cutting off bottom
                left = 0
                right = width
                top = 0
                bottom = width
                img = img.crop((left, top, right, bottom))
                img.thumbnail((300, 300))
                img.save(self.profile_pic.path)
            else:
                # already square
                img.thumbnail((300, 300))
                img.save(self.profile_pic.path)

        elif width > 300 and height == 300:
            left = (width - 300) / 2
            right = (width + 300) / 2
            top = 0
            bottom = 300
            img = img.crop((left, top, right, bottom))
            img.save(self.profile_pic.path)

        elif width > 300 and height < 300:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.save(self.profile_pic.path)

        elif width < 300 and height > 300:
            # most potential for disaster
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))
            img.save(self.profile_pic.path)

        elif width < 300 and height < 300:
            if height < width:
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img = img.crop((left, top, right, bottom))
                img.save(self.profile_pic.path)
            elif width < height:
                height = width
                left = 0
                right = width
                top = 0
                bottom = height
                img = img.crop((left, top, right, bottom))
                img.save(self.profile_pic.path)
            else:
                img.save(self.profile_pic.path)

        elif width == 300 and height > 300:
            # potential for disaster
            left = 0
            right = 300
            top = 0
            bottom = 300
            img = img.crop((left, top, right, bottom))
            img.save(self.profile_pic.path)

        elif width == 300 and height < 300:
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.save(self.profile_pic.path)

        elif width < 300 and height == 300:
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))
            img.save(self.profile_pic.path)

        elif width and height == 300:
            img.save(self.profile_pic.path)




