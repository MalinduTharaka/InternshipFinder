from django.contrib import admin
from .models import cv,job,company,student,Interview,pending

# Register your models here.

admin.site.register(cv)
admin.site.register(job)
admin.site.register(company)
admin.site.register(student)
admin.site.register(Interview)
admin.site.register(pending)

