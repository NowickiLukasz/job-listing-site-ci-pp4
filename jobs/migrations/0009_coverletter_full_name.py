# Generated by Django 3.2.13 on 2022-06-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_remove_coverletter_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='full_name',
            field=models.CharField(default='Enter Full Name', max_length=150),
        ),
    ]