from django.db import models
from  goods.models import GoodsInfo
from  user.models import UserInfo
# Create your models here.


class Cart(models.Model):
    goods = models.ForeignKey(GoodsInfo,on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    count = models.IntegerField(default=1,verbose_name='数量')
    subtotal = models.FloatField(verbose_name='价格小计')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')