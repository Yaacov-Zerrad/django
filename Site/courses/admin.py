from django.contrib import admin
from .models import Courses




class AdminCourse(admin.ModelAdmin):
    """for view in admin"""
    list_display = ('title', 'content', 'activate', )
    
# enregistre table    
admin.site.register(Courses, AdminCourse)
