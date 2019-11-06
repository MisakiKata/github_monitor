## GITHUB_MONTIOR

>   python3 + Django 2.2.6 + supervisord

1.  环境由简单的Django完成，外加一个HTML展示模板
2.  GitHub的爬虫由supervisord来维护，需要修改配置文件内的信息，可以改成/var/run路径
3.  pip安装如下的文件即可

爬虫需要账号密码模拟登陆，进程为五分钟一次。是否扫描根据任务数据里保存的时间来做判断。

修改任务只需要在编辑里输入任务名，直接输入其他参数更新即可。

数据库采用MySQL5.7。

```
python3 manager.py createsuperuser
python3 manager.py makemigrations
python3 manager.py migrate
登陆后台添加一个可以登陆前端的账号即可。
```



首界面

![1573011489137](README.assets/1573011489137.png)

未处理信息

![1573011512652](README.assets/1573011512652.png)

全部信息

![1573011525234](README.assets/1573011525234.png)

界面由于对js了解较少，没有采用比较nodejs类前端框架，当然也可以修改为自己喜欢的界面。

食用简单，望喜欢。