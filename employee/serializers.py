from django.contrib.auth.models import User
from rest_framework import serializers


class EmployeeSerializer( serializers.Serializer ):

    class Meta:
        model = User
        fields = "__all__"


