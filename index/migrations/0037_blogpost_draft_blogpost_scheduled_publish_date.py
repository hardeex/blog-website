# Generated by Django 4.2.1 on 2023-06-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0036_alter_blogcategory_name_delete_jobpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='scheduled_publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
