# Generated by Django 3.2.13 on 2022-07-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_joblisting_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverletter',
            name='title',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.CharField(choices=[('MR', 'MR'), ('MS', 'MS'), ('MRS', 'MRS')], max_length=10),
        ),
    ]
