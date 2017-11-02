# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProjectStatus( models.Model ):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'ProjectStatus'


class Approval( models.Model ):
    approver = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_on = models.DateTimeField()
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)

    class Meta:
        db_table = 'Approval'


class Project( models.Model ):
    name = models.CharField(max_length=30)
    description = models.TextField()
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    approvers = models.ManyToManyField(Approval)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Project'


class ProjectTeam( models.Model ):
    name = models.CharField(max_length=30)
    leads = models.ManyToManyField(User, related_name='project_leads')
    members = models.ManyToManyField(User, related_name='project_members')
    project = models.ForeignKey(Project)

    class Meta:
        db_table = 'ProjectTeam'