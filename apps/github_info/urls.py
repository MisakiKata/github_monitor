from django.urls import path
from .views import github_info, deal_info, ignore_info, github_total, dash


info_urlpatterns = [
    path('getinfo/', github_info, name='getinfo'),
    path('dealinfo/', deal_info, name='dealinfo'),
    path('ignore/', ignore_info, name='ignore'),
    path('total/', github_total, name='total'),
    path('dashboard/', dash, name='dashboard'),

]