# Generated by Django 3.2.13 on 2022-06-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_alter_coverletter_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverletter',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]