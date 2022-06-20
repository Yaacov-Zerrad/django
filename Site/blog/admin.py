from django.contrib import admin
from .models import Articles




class AdminArticle(admin.ModelAdmin):
    """for view in admin"""
    list_display = ('title', 'content', 'activate', )
    
# enregistre table    
admin.site.register(Articles, AdminArticle)
