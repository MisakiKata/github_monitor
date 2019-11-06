from django.urls import path
from apps.github_task import views


urlpatterns = [
    path('edit/', views.edittask, name='edit'),
    path('', views.task, name='task'),
    path('all/', views.all_task, name='alltask'),
    path('delitem/', views.delitem, name='delitem')
]