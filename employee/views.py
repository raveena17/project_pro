# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LoginView( APIView ):

    def post(self, request, format=None):
        user = authenticate( request = request )
        if user is not None:
            return Response( status = status.HTTP_200_OK )
        else:
            return Response( status = status.HTTP_404_NOT_FOUND )


