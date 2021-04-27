from django.contrib import admin
from .models import Student, Score
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.site_header = 'Ahmed Alaa'
admin.site.site_title = 'Ahmed Alaa Is Admin'





@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    pass



admin.site.register(Score)