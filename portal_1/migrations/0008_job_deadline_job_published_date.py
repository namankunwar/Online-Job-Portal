# Generated by Django 4.0.5 on 2022-07-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_1', '0007_remove_job_position_name_job_experience_job_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
    ]
