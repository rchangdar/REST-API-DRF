from django.contrib import admin
from .models import Company, Student


# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'roll', 'city']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['name','type','empcount','location']
    