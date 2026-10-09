from django.contrib import admin

# Register your models here.
from app.models import student,Course
admin.site.register(student)
admin.site.register(Course)