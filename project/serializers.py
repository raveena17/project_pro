from rest_framework import serializers

from .models import Project, ProjectStatus


class ProjectSerializer( serializers.ModelSerializer ):

    class Meta:
        model = Project
        fields = "__all__"

class ProjectStatusSerializer( serializers.ModelSerializer ):

    class Meta:
        model = ProjectStatus
        fields = "__all__"
