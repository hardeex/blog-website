# Generated by Django 3.2.12 on 2023-05-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_alter_blogpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
