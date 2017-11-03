from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^list/$', views.ProjectList.as_view(), name='project_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name="project_detail"),
    url(r'^status/$', views.ProjectStatusView.as_view(), name='project_status')
]