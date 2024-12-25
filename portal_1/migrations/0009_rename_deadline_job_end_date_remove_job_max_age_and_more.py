# Generated by Django 4.0.5 on 2022-08-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_1', '0008_job_deadline_job_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='deadline',
            new_name='end_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='max_age',
        ),
        migrations.RemoveField(
            model_name='job',
            name='min_age',
        ),
        migrations.AddField(
            model_name='job',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
