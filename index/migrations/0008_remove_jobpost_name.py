# Generated by Django 3.2.12 on 2023-05-28 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_rename_author_jobpost_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='name',
        ),
    ]
