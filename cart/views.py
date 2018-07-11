from django.shortcuts import render
from cart.models import Cart
from user.models import UserInfo
from goods.models import GoodsInfo
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def cart(request,pageindex):
    '''
    进入购物车页面
    :param request:
    :return:
    '''
    username = request.session['username']
    try:
        user = UserInfo.objects.get(username=username)
        cart_list = Cart.objects.filter(user=user).order_by('-add_time')
        num = request.session['num']
        p = Paginator(cart_list,4)
        pageindex = int(pageindex)
        page = p.page(pageindex)
        return render(request,'cart/cart.html',{'username':username,'cart_list':page,'num':num})
    except Exception as e:
        print(e)
        return render(request,'user/login.html')

def add_cart(request,goodsid,count):
    '''
    添加商品到购物车
    :param request:
    :return:
    '''
    user = UserInfo.objects.get(username=request.session['username'])
    goods = GoodsInfo.objects.get(id=goodsid)
    try:
        cartinfo = Cart.objects.get(Q(user=user) & Q(goods=goods))
        cartinfo.count += int(count)
        cartinfo.subtotal = float(cartinfo.count) * float(goods.price)
        cartinfo.save()
    except Exception as e:
        print(e)
        cartinfo = Cart(goods = goods,count=count,user=user)
        cartinfo.subtotal = float(count) * float(goods.price)
        cartinfo.save()
    return HttpResponse('添加成功')

def cart_del(request,cart_id):
    '''
    删除购物车条目
    :param request:
    :return:
    '''
    cart_id = cart_id
    status = 'ok'
    count = 0
    try:
        cart = Cart.objects.get(id=cart_id)
        if cart.count > 1:
            count = cart.count - 1
            cart.count = count
            cart.subtotal = float(cart.count) * float(cart.goods.price)
            cart.save()
            subtotal = cart.subtotal
        else:
            count = 0
            subtotal = 0
            cart.delete()
    except Exception as e:
        status = 'error'
        print(e)
    return JsonResponse({'status':status,'count':count,'subtotal':subtotal})

def cart_chg(request,cart_id,count):
    '''
    购物车修改
    :param request:
    :return:
    '''
    cart_id = cart_id
    status = 'ok'
    count = int(count)
    try:
        cart = Cart.objects.get(id=cart_id)
        if count > 0:
            cart.count = count
            cart.subtotal = float(cart.count) * float(cart.goods.price)
            cart.save()
            subtotal = cart.subtotal
        else:
            count = 0
            subtotal = 0
            cart.delete()
    except Exception as e:
        count = 0
        subtotal = 0
        status = 'error'
        print(e)
    return JsonResponse({'status': status, 'count': count, 'subtotal': subtotal})