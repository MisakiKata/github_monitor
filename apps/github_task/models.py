from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class edit_task(models.Model):
    """编辑任务"""
    task_name = models.CharField(max_length=100, verbose_name='任务名')
    word = models.CharField(verbose_name='关键词', max_length=200)
    warename = models.CharField(verbose_name='忽略仓库', max_length=200)
    ignorance = models.CharField(verbose_name='忽略账号', max_length=200)
    num = models.IntegerField(verbose_name='页数')
    time = models.IntegerField(verbose_name='时间间隔', null=True)
    marks = models.TextField(verbose_name='备注')
    username = models.CharField(verbose_name='用户名', max_length=50, default='')
    password = models.CharField(verbose_name='密码', max_length=50, default='')
    end_time = models.DateTimeField(verbose_name='结束时间', default=datetime.now)

    class Meta:
        verbose_name = '编辑任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_name


