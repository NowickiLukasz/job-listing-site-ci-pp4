# Generated by Django 3.2.13 on 2022-06-15 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_coverletter_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='slug',
            field=models.CharField(max_length=150),
        ),
    ]
