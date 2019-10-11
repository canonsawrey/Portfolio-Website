from django.contrib import admin
from .models import Project, DescriptionItem, Image
# Register your models here.


class ImageAdmin(admin.StackedInline):
    model = Image


class DescriptionItemAdmin(admin.TabularInline):
    model = DescriptionItem


class ProjectAdmin(admin.ModelAdmin):
    inlines = [DescriptionItemAdmin, ImageAdmin]


admin.site.register(Project, ProjectAdmin)
