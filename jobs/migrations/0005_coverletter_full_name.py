# Generated by Django 3.2.13 on 2022-06-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_joblisting_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='full_name',
            field=models.CharField(default='Enter Full Name', max_length=150),
        ),
    ]
