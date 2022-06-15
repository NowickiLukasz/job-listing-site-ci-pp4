# Generated by Django 3.2.13 on 2022-06-14 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('location', models.CharField(max_length=300)),
                ('salary', models.SmallIntegerField()),
                ('position_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')], max_length=20)),
                ('description', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('composed_status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('saves', models.ManyToManyField(blank=True, related_name='saved_jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoverLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('location', models.CharField(max_length=300)),
                ('position_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')], max_length=20)),
                ('salary', models.SmallIntegerField()),
                ('cover_letter', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('jobs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='jobs.joblisting')),
            ],
        ),
    ]
