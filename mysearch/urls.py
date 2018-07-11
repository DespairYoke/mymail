'''
@Time    : 2018/5/17 19:48
@Author  : Chen Xuge
@Site    : 
@File    : urls.py
@Software: PyCharm

'''
from django.conf.urls import url
from . import views

app_name = 'mysearch'
urlpatterns = [
    url(r'mysearch$',views.mysearch,name='mysearch'),
]

