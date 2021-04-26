from django.contrib import admin
from .models import Student, Score
# Register your models here.

admin.site.site_header = 'Ahmed Alaa'
admin.site.site_title = 'Ahmed Alaa Is Admin'


class StudentAdmin(admin.ModelAdmin):
    fields = ['name','title','body']
    list_display = ['name', 'title','body']
    list_display_links = ['name','body']
    list_editable = ['title']
    list_filter = ['name','title']
    search_fields = ['name','title']


admin.site.register(Student, StudentAdmin)



admin.site.register(Score)