from django.contrib import admin
from website.models import Category, Project

# Register your models here.

admin.site.register(Category)
#admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'category', 'image', 'pub_date')