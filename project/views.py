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

class ProjectStatusView( APIView ):

    def get(self, request, format=None):
        status_list = ProjectStatus.objects.all()
        serializer = ProjectStatusSerializer(status_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
