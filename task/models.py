# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from project.models import Project

# Create your models here.
class TaskStatus( models.Model ):
    name = models.CharField(max_length=60)

    class Meta:
        db_table = "TaskStatus"


class Task( models.Model ):
    name = models.CharField(max_length=60)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_to")
    assigned_By = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_by")
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, default='CREATED')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        db_table = "Task"