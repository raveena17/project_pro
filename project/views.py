# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Project, ProjectStatus
from .serializers import ProjectSerializer, ProjectStatusSerializer


class ProjectList( generics.ListCreateAPIView ):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectStatusList( generics.ListCreateAPIView ):
    queryset = ProjectStatus.objects.all()
    serializer_class = ProjectStatusSerializer

class ProjectStatusDetail( generics.RetrieveUpdateDestroyAPIView ):
    queryset = ProjectStatus.objects.all()
    serializer_class = ProjectStatusSerializer