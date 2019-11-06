from django.db import models

# Create your models here.

class Warename(models.Model):
    AVATOR = {
        (1, '已处理'),
        (2, '已忽略'),
        (0, '未处理'),
    }
    name = models.CharField(verbose_name='仓库名', max_length=500)
    filename = models.CharField(verbose_name='文件名', max_length=1000)
    time = models.CharField(verbose_name='更新时间', max_length=50, null=True)
    marks = models.CharField(verbose_name='备注', max_length=500, blank=True)
    dealwith = models.IntegerField(verbose_name='处置', choices=AVATOR, default=0)

    class Meta:
        verbose_name = '仓库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name