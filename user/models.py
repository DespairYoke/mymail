from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    pwd = models.CharField(max_length=20, verbose_name='密码')
    email = models.CharField(max_length=30, default='xxx@163.com', verbose_name='邮箱')
    phone = models.CharField(max_length=11, default='15555555555', verbose_name='手机号')


class Addresss(models.Model):
    recv = models.CharField(max_length=50,verbose_name='收件人')
    phone = models.CharField(max_length=11,verbose_name='联系方式',null=True)
    province = models.CharField(max_length=50,verbose_name='省份')
    city = models.CharField(max_length=50,verbose_name='城市')
    country = models.CharField(max_length=50,verbose_name='县区',null=True)
    intro = models.TextField(verbose_name='详细地址')
    status = models.BooleanField(default=False)
    postcode = models.CharField(max_length=6,verbose_name='邮编',default='000000')
    username = models.ForeignKey(UserInfo,on_delete=models.CASCADE)

class Areainfo(models.Model):
    title = models.CharField(max_length=50,verbose_name='地址')
    parea = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)