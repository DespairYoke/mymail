'''
@Time    : 2018/5/18 10:35
@Author  : Chen Xuge
@Site    : 
@File    : urls.py
@Software: PyCharm
# code is far away from bugs with the god animal protecting

'''

"""mymail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name='myorder'
urlpatterns = [
    # 结算确认
    url('^place_order/(\d+)$', views.place_order, name='place_order'),
    # 生成订单
    url('^myorder_done/$', views.myorder_done, name='myorder_done'),
    # 订单列表
    url('^myorder_list/(\d+)/$', views.myorder_list, name='myorder_list'),
    # 订单详情
    url('^myorder_info/(?P<order_id>\d+)/$', views.myorder_info, name='myorder_info'),
]
