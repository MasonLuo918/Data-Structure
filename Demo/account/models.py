from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userprofile(models.Model):

    motto = models.TextField(blank=True)
    HeadImage = models.ImageField(upload_to="Image/%Y/%m/%d",blank=True)
    WeCheat = models.ImageField(upload_to="WeCheat/%Y/%m/%d",blank=True)
    phone = models.CharField(max_length=11,blank=True)
    user = models.OneToOneField(User,related_name="user_profile")
    School = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return "{}-profile".format(self.user.username)

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name="验证码")
    email = models.CharField(max_length=50,verbose_name="邮箱")
    send_time = models.DateTimeField(verbose_name="发送时间",auto_now_add=True)
    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}({})'.format(self.code,self.email)
