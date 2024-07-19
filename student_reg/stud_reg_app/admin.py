from django.contrib import admin
from stud_reg_app.models import *
# Register your models here.


@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('usn', 'name')
    ordering = ('usn', )
    search_fields = ('name', )

@admin.register(course)
class courseAdmin(admin.ModelAdmin):
    list_display = ('courseCode', 'courseName')
    ordering = ('courseCode', )
    search_fields = ('courseName', )
