# Generated by Django 5.0 on 2024-01-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=255, verbose_name='ID')),
                ('author', models.CharField(max_length=255, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='ID')),
                ('page_count', models.IntegerField(default=10, verbose_name='Page Count')),
                ('category', models.CharField(max_length=50, verbose_name='category')),
                ('shelf_location', models.CharField(max_length=50, verbose_name='shelflocation')),
                ('published_date', models.DateField(verbose_name='published date')),
                ('is_in_stock', models.BooleanField(default=True, verbose_name='is in stock')),
                ('date_checked_out', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Library',
                'verbose_name_plural': 'Library',
                'db_table': 'library',
            },
        ),
    ]
