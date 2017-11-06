from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^list/$', views.ProjectList.as_view(), name='project_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name="project_detail"),
    url(r'^status/list/$', views.ProjectStatusList.as_view(), name='project_status_list'),
    url(r'^status/(?P<pk>[0-9]+)/$', views.ProjectStatusDetail.as_view(), name='project_status_detail')
]