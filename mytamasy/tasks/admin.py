from django.contrib import admin
from .models import Task, BugTask, FeatureTask

admin.site.register(Task)
admin.site.register(BugTask)
admin.site.register(FeatureTask) 