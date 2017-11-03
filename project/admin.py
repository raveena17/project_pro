# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ProjectStatus, Project, Approval
# Register your models here.

admin.site.register(ProjectStatus)
admin.site.register(Project)
admin.site.register(Approval)