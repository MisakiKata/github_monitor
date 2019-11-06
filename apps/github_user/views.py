from django.shortcuts import render, redirect
from .models import UserList
# Create your views here.


def index(request):
    """首页"""
    if request.session.get('is_login') == '1':

        return redirect('/table/dashboard')
    else:
        return redirect('/login')
    pass


def login(request):
    """登陆"""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username.strip() and password:
            try:
                user = UserList.objects.get(username=username)
            except:
                message = "用户不存在"
                return render(request, 'login.html', locals())
            if user.password == password:
                request.session['is_login'] = '1'
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                request.session.set_expiry(3600)
                return redirect('/table/dashboard')
            else:
                message = '密码不正确'
                return render(request, 'login.html', locals())
        else:
            message='请输出正确格式的用户名和密码'
            return render(request, 'login.html', locals())
    elif request.method == "GET":
        return render(request, 'login.html')
    return redirect('/login')


def logout(request):
    """退出"""
    if request.session.get('is_login') != '1':
        return redirect('/login')

    pass

