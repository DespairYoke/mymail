'''
@Time    : 2018/5/14 10:35
@Author  : Chen Xuge
@Site    : 
@File    : urls.py
@Software: PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛

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

app_name='user'
urlpatterns = [
    url('register$',views.register,name='register'),
    url('register_handel$',views.register_handel,name='register_handel'),
    url('login$',views.login,name='login'),
    url('login_handel$',views.login_handel,name='login_handel'),
    url('logout$',views.logout,name='logout'),
    url('user_center_info$',views.user_center_info,name='user_center_info'),
    url('user_center_order$',views.user_center_order,name='user_center_order'),
    url('user_center_site/$',views.user_center_site,name='user_center_site'),
    url('user_chg_pwd$',views.user_chg_pwd,name='user_chg_pwd'),
    url('user_chg_pwd_handel$',views.user_chg_pwd_handel,name='user_chg_pwd_handel'),
    url('addaddress$',views.addaddress,name='addaddress'),
    url('del_address/(\d+)/$',views.del_address,name='del_address'),
    url('pro/$',views.pro,name='pro'),
    url('city(\d+)/$',views.city,name='city'),
]
