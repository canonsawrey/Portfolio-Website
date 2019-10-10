from django.db import models
import datetime


class Sample(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    abstract = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    github_link = models.CharField(max_length=100)


class DescriptionItem(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

