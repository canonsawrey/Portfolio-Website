from django.db import models


class Job(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    abstract = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


class DescriptionItem(models.Model):
    project = models.ForeignKey(Job, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)


