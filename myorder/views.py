from django.shortcuts import render,redirect
from django.urls import reverse
from user.models import Addresss,UserInfo
from cart.models import Cart
from goods.models import GoodsInfo
from .models import OrderInfo,MyOrderItem
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.


def place_order(request,flag):
    '''
    进入结算确认页面
    :param request:
    :return:
    '''
    username = request.session['username']
    try:
        user = UserInfo.objects.get(username=username)
        address_list = Addresss.objects.filter(username=user)
        status = 0
        if flag == '1':
            cartid_list = request.POST.getlist('cartinfo.id')
            total = request.POST.get('total')
            total_count = request.POST.get('total_count')
            if float(total)>50:
                totals = total
                status = 1
            else:
                totals = float(total) + 10
            # print(total)
            # print(total_count)
            # print(cartid_list)
            cartinfo_list = Cart.objects.filter(id__in=cartid_list)
            context = {'username':username,'address_list':address_list,'cartinfo_list':cartinfo_list,'total':total,'total_count':total_count,'totals':totals,'status':status}
            return render(request,'myorder/place_order.html',context)
        if flag == '0':
            # cartinfo_list = Cart.objects.get(id=1)
            good_id = request.POST.get('good_id')
            print(good_id)
            good = GoodsInfo.objects.get(id=good_id)
            num = request.POST.get('num')
            subtotal = float(num) * float(good.price)
            # print(good_id)
            # print(num)
            cartinfo = Cart(count=num,subtotal=subtotal,goods=good,user=user)
            cartinfo.save()
            cartinfo_list = []
            cartinfo_list.append(cartinfo)
            if subtotal > 50:
                totals = subtotal
                status = 1
            else:
                totals = float(subtotal) + 10
            # print(cartinfo_list)
            context = {'username': username, 'address_list': address_list,'cartinfo_list':cartinfo_list,'total':subtotal,'total_count':num,'totals':totals,'status':status}
            return render(request, 'myorder/place_order.html', context)
    except Exception as e:
        print(e)
        return render(request, 'user/login.html')



def myorder_done(request):
    '''
    生成订单
    :param request:
    :return:
    '''
    username = request.session['username']
    user = UserInfo.objects.get(username = username)
    addressid = request.POST.get('address')
    # 根据付款方式判断是否付款
    pay_style = request.POST.get('pay_style')
    address = Addresss.objects.get(id=addressid)
    order_address = address.province+'-'+address.city+'-'+address.country+'-'+address.intro+'-'+address.recv+'-'+address.postcode+'-'+address.phone
    # total_count = request.POST.get('total_count')
    totals = request.POST.get('totals')
    # print(order_address)
    # print(total_count)
    # print(totals)
    orderinfo = OrderInfo()
    orderinfo.order_address = order_address
    orderinfo.order_total = totals
    orderinfo.order_user = user
    # TODO 判断是否付款
    print(int(pay_style))
    if int(pay_style) == 1:
        orderinfo.status = True
    else:
        orderinfo.status = False
    orderinfo.save()
    cartinfo_list =  request.POST.getlist('cartinfo_id')
    # print(cartinfo_list)
    for cartinfo_id in cartinfo_list:
        mycart = Cart.objects.get(id =cartinfo_id)
        myorder = MyOrderItem(goods_img=mycart.goods.pic,goods_name=mycart.
                              goods.name,goods_price=mycart.goods.price,goods_count=mycart.count,
                              goods_subtotal=mycart.subtotal,myorder=orderinfo)
        myorder.save()
        # 订单生成，删除购物车条目
        mycart.delete()
    return redirect(reverse('myorder:myorder_info',kwargs={'order_id':orderinfo.id}))


def myorder_list(request,pindex):
    '''
    订单列表
    :param request:
    :return:
    '''
    username = request.session['username']
    try :
        user = UserInfo.objects.get(username=username)
        orderlist = OrderInfo.objects.filter(order_user=user).order_by('-order_time')
        # print(orderlist)
        p =Paginator(orderlist,10)
        list = p.page(pindex)
        return render(request,'user/user_center_order.html',{'orderlist':list,'username':username})
    except Exception as e:
        print(e)
        return render(request, 'user/login.html')


def myorder_info(request,order_id):
    '''
    订单详情
    :param request:
    :return:
    '''
    myorder = OrderInfo.objects.get(id=order_id)
    username = request.session['username']
    return render(request,'myorder/myorder_info.html',{'username':username,'myorder':myorder})