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

class TaskStatusView( APIView ):

    def get(self, request, format=None):
        status_list = TaskStatus.objects.all()
        serializer = TaskStatusSerializer(status_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
