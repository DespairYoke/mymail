from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from user.models import *
from django.db.models import Q
from cart.models import Cart
# Create your views here.


def register(request):
    '''
    进入注册页面
    :param request:
    :return:
    '''
    return render(request, 'user/register.html')


def register_handel(request):
    '''
    处理注册输入的信息
    :param request:
    :return:
    '''
    # 获取相关信息
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        print(username, pwd, email, phone)
        result = UserInfo.objects.filter(username=username)
        if result.exists() or len(username) == 0 or len(pwd) == 0 or len(email) == 0 or len(phone) == 0:
            return render(request, 'user/register.html', {'flag': '0'})
        else:
            result.create(username=username, pwd=pwd, email=email, phone=phone, )
            return render(request, 'user/login.html')


def login(request):
    '''
    进入登录页面
    :param request:
    :return:
    '''
    request.session['num'] = ''
    return render(request, 'user/login.html')


def login_handel(request):
    '''
    处理登录信息
    :param request:
    :return:
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        # print(username,pwd)
        try:
            user = UserInfo.objects.get(Q(username=username) & Q(pwd=pwd))
            cart_list = Cart.objects.filter(user=user)
            num = cart_list.count()
            request.session['num'] = num
            request.session['username'] = username

            # request.session.set_expiry(0)
            return HttpResponseRedirect(reverse('goods:index'))
        except Exception as e:
            print(e)
            return render(request, 'user/login.html', {'flag': 0})


def logout(request):
    '''
    退出登录
    :param request:
    :return:
    '''
    request.session['username'] = ''
    request.session['num'] = ''
    return HttpResponseRedirect(reverse('goods:index'))


def user_center_info(request):
    '''
    进入个人中心
    :param request:
    :return:
    '''
    username = request.session['username']
    try:
        result = UserInfo.objects.get(username=username)
        address = Addresss.objects.get(username_id=result.id, status=True)
        cartlist = Cart.objects.filter(user=result).order_by('-add_time')[:5]
        context = {'username': username, 'user': result, 'address': address, 'cartlist': cartlist}
        return render(request, 'user/user_center_info.html', context)
    except Exception as e:
        print(e)
        return render(request, 'user/login.html')


def user_center_order(request):
    '''

    :param request:
    :return:
    '''

    username = request.session['username']
    if username == '':
        return render(request, 'user/login.html')
    else:
        return render(request, 'user/user_center_order.html', {'username': username})


def user_center_site(request):
    '''
    进入地址页面
    :param request:
    :return:
    '''
    username = request.session['username']
    try:
        id = UserInfo.objects.get(username=username).id
        addresslist = Addresss.objects.filter(username_id=id)
        return render(request, 'user/user_center_site.html', {'username': username, 'addresslist': addresslist})
    except Exception as e:
        print(e)
        return render(request, 'user/user_center_site.html', {'username': username})


def user_chg_pwd(request):
    '''
    进入修改密码
    :param request:
    :return:
    '''
    username = request.session['username']
    return render(request, 'user/user_chg_pwd.html', {'username': username})


def user_chg_pwd_handel(request):
    '''
    修改密码处理
    :param request:
    :return:
    '''
    if request.method == 'POST':
        username = request.session['username']
        opwd = request.POST.get('opwd')
        pwd = request.POST.get('pwd')
        try:
            result = UserInfo.objects.get(Q(username=username) & Q(pwd=opwd))
            result.pwd = pwd
            result.save()
            return render(request, 'user/user_chg_pwd_handel.html', {'username': username})
        except Exception as e:
            print(e)
            return render(request, 'user/user_chg_pwd.html')


def pro(request):
    '''
    动态加载省级数据
    :param request:
    :return:
    '''
    # print('pro')
    prolist = Areainfo.objects.filter(parea__isnull=True)

    list = []
    for item in prolist:
        list.append([item.id, item.title])  # [1,'北京']
    return JsonResponse({'data': list})


def city(request, id):
    '''
    加载地市或者县区的数据
    :param request:
    :param id:
    :return:
    '''
    citylist = Areainfo.objects.filter(parea_id=id)
    list = []
    for item in citylist:
        list.append({'id': item.id, 'title': item.title})
    return JsonResponse({'data': list})


def addaddress(request):
    '''
    处理添加地址页面
    :param request:
    :return:
    '''
    username = request.session['username']
    try:
        user = UserInfo.objects.get(username=username)
    except Exception as e:
        print(e)
    # 2 接收表单数据
    if request.method == 'POST':
        recv = request.POST.get('recv')
        phone = request.POST.get('phone')
        postcode = request.POST.get('postcode')
        pro_id = request.POST.get('pro')
        city_id = request.POST.get('city')
        dis_id = request.POST.get('dis')
        intro = request.POST.get('intro')
        status = request.POST.get('status')
        # 3 获取省、市、县区的模型对象
        pro = None
        if pro_id != None:
            try:
                pro = Areainfo.objects.get(id=pro_id)
            except Exception as e:
                print(e)
        city = None
        if city_id != None:
            try:
                city = Areainfo.objects.get(id=city_id)
            except Exception as e:
                print(e)
        dis = None
        if dis_id != None:
            try:
                dis = Areainfo.objects.get(id=dis_id)
            except Exception as e:
                print(e)
        # 4 创建收货地址的对象，设置属性的值
        addr = Addresss()
        addr.recv = recv
        addr.province = pro.title
        addr.city = city.title
        addr.country = dis.title
        addr.intro = intro
        addr.phone = phone
        addr.postcode = postcode
        if status == 'on':
            # 5如果新的地址是默认地址，更新
            id = UserInfo.objects.get(username=username).id
            addresslist = Addresss.objects.filter(username_id=id)
            for address in addresslist:
                address.status = False
                address.save()
            addr.status = True
        else:
            addr.status = False
        # 6 设置user属性，是那个用户的收货地址
        addr.username = user
        addr.save()
    return HttpResponseRedirect(reverse('user:user_center_site'))


def del_address(request, address_id):
    '''
    删除地址
    :param request:
    :return:
    '''
    address = Addresss.objects.get(id=address_id)
    if address.status == 0:
        address.delete()
    else:
        newaddress = Addresss.objects.filter(username=address.username).first()
        newaddress.status = 1
        newaddress.save()
        address.delete()
    return JsonResponse({'status': 'ok'})
