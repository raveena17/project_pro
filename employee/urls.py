from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^list/', views.UsersView.as_view(), name='get_users'),
]