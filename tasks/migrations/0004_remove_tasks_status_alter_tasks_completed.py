# Generated by Django 4.2.1 on 2023-06-29 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_tasks_completed_alter_tasks_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='status',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='completed',
            field=models.CharField(default='No', max_length=150),
        ),
    ]
