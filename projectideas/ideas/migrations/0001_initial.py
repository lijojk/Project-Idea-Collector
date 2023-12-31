# Generated by Django 4.2.2 on 2023-06-28 09:34

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('courses', models.CharField(max_length=150)),
                ('cr_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('technology', models.CharField(max_length=50)),
                ('cr_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Technology',
            },
        ),
        migrations.CreateModel(
            name='ProjectIdeas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('project_Type', models.CharField(choices=[(0, 'Mini Project'), (1, 'Main Project'), (2, 'Live Project')], default='1', max_length=20)),
                ('description', models.TextField()),
                ('project_Title', models.CharField(max_length=120)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.course')),
                ('cr_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.technology')),
            ],
            options={
                'verbose_name_plural': 'Project Idea',
            },
        ),
    ]
