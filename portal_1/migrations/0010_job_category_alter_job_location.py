# Generated by Django 4.0.5 on 2022-08-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_1', '0009_rename_deadline_job_end_date_remove_job_max_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
