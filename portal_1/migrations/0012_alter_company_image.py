# Generated by Django 4.0.5 on 2022-08-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_1', '0011_company_remove_job_image_alter_job_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
