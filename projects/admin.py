from django.contrib import admin
from .models import Project, About

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','created_on')
    list_filter = ("created_on",)
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(About, AboutAdmin)