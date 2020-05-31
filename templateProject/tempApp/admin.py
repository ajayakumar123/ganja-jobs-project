from django.contrib import admin
from tempApp.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):

    list_display = ['name','marks','country']


admin.site.register(Student,StudentAdmin)
