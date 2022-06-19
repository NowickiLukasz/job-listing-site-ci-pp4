# Generated by Django 3.2.13 on 2022-06-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_coverletter_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='submited_letter',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
