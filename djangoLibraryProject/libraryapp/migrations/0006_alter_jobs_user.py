# Generated by Django 5.0 on 2024-02-25 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0005_remove_jobs_id_alter_jobs_jobid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]
