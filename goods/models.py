from django.db import models

# Create your models here.


class GoodsInfo(models.Model):
    name = models.CharField(max_length=30,verbose_name='商品名称')
    content = models.TextField(default='掌柜非常懒，什么也没有留',verbose_name='商品介绍',null=True)
    cate = models.ForeignKey('CategeoryInfo',on_delete=models.CASCADE,verbose_name='商品分类',null=True)
    sku = models.IntegerField(default=0,verbose_name='库存',null=True)
    sale = models.IntegerField(default=0,verbose_name='销量',null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='价格',null=True)
    unit = models.CharField(max_length=20,default='',verbose_name='单位',null=True)
    pic = models.ImageField(upload_to='goods/',default='goods/default.jpg',verbose_name='商品图片',null=True)
    #shops = models.ForeignKey('ShopInfo',on_delete=models.CASCADE,verbose_name='所属店铺')
    add_date = models.DateTimeField(auto_now_add=True,verbose_name='上架时间')
    pv = models.IntegerField(default=0,verbose_name='访问量',null=True)
    recommond = models.BooleanField(default=False,verbose_name='商品推荐')


class CategeoryInfo(models.Model):
    cate = models.CharField(max_length=20,default='',verbose_name='商品分类',null=True)