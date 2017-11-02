# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer


class LoginView( APIView ):

    def post(self, request, format=None):
        user = authenticate( **request.data )
        if user is not None:
            login(request, user)
            #token = Token.objects.create( user=user )
            return Response( status=status.HTTP_200_OK )
        else:
            return Response( status=status.HTTP_404_NOT_FOUND )



class LogoutView( APIView ):

    def get(self, request, format=None):
        logout( request )
        return Response( status=status.HTTP_200_OK )


class UsersView( APIView ):

    def post(self, request, format=None):
        query = Q()
        if 'group_names' in request.data:
            query &= Q(groups__name__in=request.data.get( 'group_names' ))
        users = User.objects.all().filter(query)
        serializer = UserSerializer(users, many=True)
        return Response( serializer.data, status=status.HTTP_200_OK )