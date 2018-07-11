from django.db import models
from user.models import UserInfo
# Create your models here.


class OrderInfo(models.Model):
    order_time = models.DateTimeField(auto_now_add=True,verbose_name='下单时间')
    order_address = models.CharField(max_length=200,verbose_name='收货地址')
    order_total = models.FloatField(verbose_name='总计金额')
    order_user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    status = models.BooleanField(default=False,verbose_name='是否付款')

class MyOrderItem(models.Model):
    goods_img = models.ImageField(upload_to='static/images/goods')
    goods_name = models.CharField(max_length=20,verbose_name='商品名称')
    goods_price = models.FloatField(verbose_name='商品单价')
    goods_count = models.IntegerField(verbose_name='商品数量')
    goods_subtotal = models.FloatField(verbose_name='商品小计')
    myorder = models.ForeignKey(OrderInfo,on_delete=models.CASCADE)
