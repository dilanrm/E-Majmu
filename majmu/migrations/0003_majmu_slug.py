# Generated by Django 3.0 on 2019-09-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majmu', '0002_remove_majmu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='majmu',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
