# Generated by Django 3.2.13 on 2022-06-22 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0016_alter_joblisting_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
