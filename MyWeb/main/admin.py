from django.contrib import admin
from .models import Project, AboutMe, ContactMessage
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title"]



admin.site.register(Project,ProjectAdmin)
