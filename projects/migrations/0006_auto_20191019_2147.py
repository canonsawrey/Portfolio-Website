# Generated by Django 2.2.6 on 2019-10-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20191010_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='languages',
            field=models.CharField(default='Kotlin', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='platforms',
            field=models.CharField(default='Android', max_length=100),
            preserve_default=False,
        ),
    ]
