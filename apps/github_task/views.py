from django.shortcuts import render, redirect
from .models import edit_task
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def edittask(request):
    """编辑任务"""
    if request.session.get('is_login') != '1':
        return redirect('/login')
    if request.method == "POST":
        task_name = request.POST.get('task_name')
        word = request.POST.get('word')
        warename = request.POST.get('warename')
        ignorance = request.POST.get('ignorance')
        num = request.POST.get('num')
        time = request.POST.get('time')
        marks = request.POST.get('marks')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            if edit_task.objects.filter(task_name='task_name'):
                if request.POST.get('word'):
                    edit_task.objects.filter(task_name=task_name).update(word=word)
                if request.POST.get('warename'):
                    edit_task.objects.filter(task_name=task_name).update(warename=warename)
                if request.POST.get('ignorance'):
                    edit_task.objects.filter(task_name=task_name).update(ignorance=ignorance)
                if request.POST.get('num'):
                    edit_task.objects.filter(task_name=task_name).update(num=num)
                if request.POST.get('time'):
                    edit_task.objects.filter(task_name=task_name).update(time=time)
                if request.POST.get('marks'):
                    edit_task.objects.filter(task_name=task_name).update(marks=marks)
                if request.POST.get('username'):
                    edit_task.objects.filter(task_name=task_name).update(username=username)
                if request.POST.get('password'):
                    edit_task.objects.filter(task_name=task_name).update(password=password)
                message = '任务更新成功'
                return render(request, 'configuration.html', locals())
            else:
                if username and password and word:
                    list = edit_task.objects.create(task_name=task_name,word=word,warename=warename,ignorance=ignorance,
                             num=num,time=time,marks=marks,username=username,password=password)
                    message = '任务添加成功'
                    return render(request, 'configuration.html', locals())
        except:
            message = '任务添加失败'
            return render(request, 'configuration.html', locals())



def all_task(request):
    """全部任务"""
    if request.session.get('is_login') != '1':
        return redirect('/login')
    if request.method == "GET":
        tasks = edit_task.objects.all()
        return render(request, 'typography.html', locals())


def task(request):
    """编辑页"""
    if request.session.get('is_login') != '1':
        return redirect('/login')
    if request.method == "GET":
        return render(request, 'configuration.html')

@csrf_exempt
def delitem(request):
    """删除任务"""
    if request.session.get('is_login') != '1':
        return redirect('/login')
    if request.method == 'POST':
        id = request.POST.get('id')
        edit_task.objects.get(id=id).delete()
        message = "任务删除成功"
        return render(request, 'typography.html', locals())
