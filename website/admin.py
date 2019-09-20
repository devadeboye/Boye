from django.contrib import admin
from website.models import Category, Project

# Register your models here.

admin.site.register(Category)
#admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # list the fields to be displayed in adminsite and how
    # to show them
    list_display = ('project_name', 'category', 'image', 'pub_date')

    # add a filter to filter projects in the adminsite
    list_filter = ('category',)