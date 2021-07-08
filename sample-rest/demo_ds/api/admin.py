from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmplyeeAdmin(admin.ModelAdmin):
    list_display=['empid','name','city','zip']