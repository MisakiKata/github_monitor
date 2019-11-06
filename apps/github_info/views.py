from django.shortcuts import render, redirect
from .models import Warename
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def github_info(request):
    """ 获取信息"""
    if request.session.get('is_login') != '1':
        return redirect('/login')
    if request.method == "GET":
        tasks = Warename.objects.filter(dealwith=0)
        return render(request, 'table.html', locals())

@csrf_exempt
def deal_info(request):
    """ 处理"""
    if request.session.get('is_login') != '1':
        return redirect('/login')
    if request.method == "POST":
        try:
            id = request.POST.get('id')
        except:
            message = '未查询到数据'
            return render(request, 'table.html', locals())
        github = Warename.objects.get(id=id)
        github.dealwith = 1
        github.save()
        message = '处置成功'
        return render(request, 'table.html', locals())

@csrf_exempt
def ignore_info(request):
    """忽略"""
    if request.session.get('is_login') != '1':
        return redirect('/login')
    if request.method == "POST":
        try:
            id = request.POST.get("id")
        except:
            message = "未查询到数据"
            return render(request, 'table.html', locals())
        github = Warename.objects.get(id=id)
        github.dealwith = 2
        github.save()
        message = "处置成功"
        return render(request, 'table.html', locals())


def github_total(request):
    """全部信息"""
    if request.session.get('is_login') != '1':
        return redirect('/login')
    if request.method == "GET":
        tasks = Warename.objects.all()
        return render(request, 'total.html', locals())


def dash(request):
    """统计表"""
    if request.session.get("is_login") != '1':
        return redirect('/login')
    if request.method == "GET":
        all = Warename.objects.all()
        deal = Warename.objects.filter(dealwith=1)
        nodeal = Warename.objects.filter(dealwith=2)
        ondeal = Warename.objects.filter(dealwith=0)
        return render(request, 'dashboard.html', locals())
