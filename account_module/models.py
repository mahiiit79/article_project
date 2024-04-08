from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile',blank=True,null=True,verbose_name='تصویر آواتار')
    email_active_code = models.CharField(max_length=100,verbose_name='کد فعال سازی ایمیل')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    phone_number = models.CharField(max_length=11,blank=True,null=True,verbose_name='شماره همراه')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta :
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        else:
            return self.email