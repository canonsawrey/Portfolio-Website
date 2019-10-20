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
    platforms = models.CharField(null=True, max_length=100)
    languages = models.CharField(null=True, max_length=100)
    blurb = models.TextField()

    def on_android(self):
        if "Android" in self.platforms:
            return True
        else:
            return False

    def on_desktop(self):
        if "Desktop" in self.platforms:
            return True
        else:
            return False

    def on_ios(self):
        if "iOS" in self.platforms:
            return True
        else:
            return False

    def on_web(self):
        if "Web" in self.platforms:
            return True
        else:
            return False

    def in_kotlin(self):
        if "Kotlin" in self.languages:
            return True
        else:
            return False

    def in_python(self):
        if "Python" in self.languages:
            return True
        else:
            return False

    def in_java(self):
        if "Java" in self.languages:
            return True
        else:
            return False

    def in_sql(self):
        if "SQL" in self.languages:
            return True
        else:
            return False



class DescriptionItem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='.projects/static/projects/images')
    caption = models.CharField(max_length=200)

