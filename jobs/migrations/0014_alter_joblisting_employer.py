# Generated by Django 3.2.13 on 2022-06-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_alter_joblisting_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='employer',
            field=models.CharField(max_length=200),
        ),
    ]
