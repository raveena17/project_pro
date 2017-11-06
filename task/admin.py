# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import TaskStatus, Task

# Register your models here.
admin.site.register(TaskStatus)
admin.site.register(Task)