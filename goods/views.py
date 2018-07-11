from django.shortcuts import render
from django.core.paginator import Paginator
from goods.models import *
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    '''
    进入商品页面
    :param request:
    :return:
    '''
    num = request.session['num']
    goodslist1 = GoodsInfo.objects.filter(cate=1).order_by('-add_date')[:4]
    goodslist2 = GoodsInfo.objects.filter(cate=2).order_by('-price')[:4]
    goodslist3 = GoodsInfo.objects.filter(cate=3).order_by('-pv')[:4]
    goodslist4 = GoodsInfo.objects.filter(cate=4).order_by('-price')[:4]
    goodslist5 = GoodsInfo.objects.filter(cate=5).order_by('-price')[:4]
    goodslist6 = GoodsInfo.objects.filter(cate=6).order_by('-price')[:4]
    recommond1 = GoodsInfo.objects.filter(Q(cate=1) & Q(recommond=1))[:3]
    recommond2 = GoodsInfo.objects.filter(Q(cate=2) & Q(recommond=1))[:3]
    recommond3 = GoodsInfo.objects.filter(Q(cate=3) & Q(recommond=1))[:3]
    recommond4 = GoodsInfo.objects.filter(Q(cate=4) & Q(recommond=1))[:3]
    recommond5 = GoodsInfo.objects.filter(Q(cate=5) & Q(recommond=1))[:3]
    recommond6 = GoodsInfo.objects.filter(Q(cate=6) & Q(recommond=1))[:3]
    pic1 = '/static/images/banner01.jpg'
    pic2 = '/static/images/banner02.jpg'
    pic3 = '/static/images/banner03.jpg'
    pic4 = '/static/images/banner04.jpg'
    pic5 = '/static/images/banner05.jpg'
    pic6 = '/static/images/banner06.jpg'
    goodslist = [{'cate_name': '新鲜水果', 'list': goodslist1,'recommond':recommond1,'pic':pic1,'id':1},
                 {'cate_name': '新鲜水产', 'list': goodslist2,'recommond':recommond2,'pic':pic2,'id':2},
                 {'cate_name': '猪牛羊肉', 'list': goodslist3,'recommond':recommond3,'pic':pic3,'id':3},
                 {'cate_name': '禽类蛋品', 'list': goodslist4,'recommond':recommond4,'pic':pic4,'id':4},
                 {'cate_name': '新鲜蔬菜', 'list': goodslist5,'recommond':recommond5,'pic':pic5,'id':5},
                 {'cate_name': '速冻食品', 'list': goodslist6,'recommond':recommond6,'pic':pic6,'id':6},
                 ]
    username = request.session['username']
    return render(request, 'goods/index.html',{'username':username, 'goodslist':goodslist,'num':num})

def detail(request,p1):
    '''
    进入商品详情
    :param request:
    :param p1:
    :return:
    '''
    num = request.session['num']
    username = request.session['username']
    good = GoodsInfo.objects.get(id=p1)
    cate_name = good.cate
    cate = cate_name.id
    goodlist = GoodsInfo.objects.filter(cate=cate).order_by('add_date')[:2]
    return render(request,'goods/detail.html',{'good':good,'cate_name':cate_name,'goodlist':goodlist,'username':username,'num':num})

def list(request,p2,pageindex):
    '''
    进入商品列表
    :param request:
    :param p2:
    :return:
    '''
    num = request.session['num']
    username = request.session['username']
    cate = CategeoryInfo.objects.get(id = p2)
    goodslist = GoodsInfo.objects.filter(cate=p2)
    p = Paginator(goodslist,10)
    pageindex = int(pageindex)
    page = p.page(pageindex)
    goodlist = goodslist.order_by('add_date')[:2]
    return render(request,'goods/list.html',{'goodslist':page,'goodlist':goodlist,'cate':cate,'username':username,'num':num})

