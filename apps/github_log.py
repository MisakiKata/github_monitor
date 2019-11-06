import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "github_monitor.settings")
django.setup()

from apps import github_login
from apps.github_info import models
from apps.github_task import models as ts
from datetime import datetime
import threading


def github(username, password, word, num, warename, ignorance):
    list = github_login.github_login(word, num)
    gitinfo = list.get_cookie(username, password)
    for nua in range(0, len(gitinfo[0])):
        for nub in range(0, 10):
            try:
                if warename != gitinfo[0][nua][nub].split('/')[2] and ignorance != gitinfo[0][nua][nub].split('/')[1] and removal(gitinfo[1][nua][nub],gitinfo[2][nua][nub]):
                    models.Warename.objects.create(name=gitinfo[0][nua][nub], filename=gitinfo[1][nua][nub], time=gitinfo[2][nua][nub])
            except Exception as e:
                print(e)


def removal(filename, time):
    if models.Warename.objects.filter(filename=filename, time=time):
        return False
    else:
        return True


def run():
    task_info = ts.edit_task.objects.all()
    for task in task_info:
        time = task.time
        nowtime = datetime.utcnow() - task.end_time.replace(tzinfo=None)
        if nowtime.seconds >= (time * 60):
            github(task.username, task.password, task.word, task.num, task.warename, task.ignorance)
            t = ts.edit_task.objects.get(id=task.id)
            t.end_time = datetime.now()
            t.save()

    timer = threading.Timer(300, run)
    timer.start()


timer = threading.Timer(60, run)
timer.start()
