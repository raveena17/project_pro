from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^list/$', views.TaskList.as_view(), name='task_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name="task_detail"),
    url(r'^status/list/$', views.TaskStatusList.as_view(), name='task_status_list'),
    url(r'^status/(?P<pk>[0-9]+)/$', views.TaskStatusList.as_view(), name='task_status_detail')
]