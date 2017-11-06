# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Task, TaskStatus
from .serializers import TaskSerializer, TaskStatusSerializer


class TaskList( generics.ListCreateAPIView ):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskStatusList( generics.ListCreateAPIView ):
    queryset = Task.objects.all()
    serializer_class = TaskStatusSerializer

class TaskStatusDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Task.objects.all()
    serializer_class = TaskStatusSerializer