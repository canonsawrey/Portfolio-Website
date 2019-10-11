from django.db import models
import os
import datetime


class Project(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(null=True, blank=True, max_length=50)
    abstract = models.CharField(max_length=300)
    goal = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    github_link = models.CharField(null=True, blank=True, max_length=100)


class DescriptionItem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='.projects/static/projects/images')
    caption = models.CharField(max_length=200)

