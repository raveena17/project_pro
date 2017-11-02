from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^list/', views.UsersByGroupView.as_view(), name='get_users'),
]