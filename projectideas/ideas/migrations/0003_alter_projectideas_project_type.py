# Generated by Django 4.2.2 on 2023-06-28 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_alter_course_cr_user_alter_projectideas_cr_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectideas',
            name='project_Type',
            field=models.CharField(choices=[('Mini Project', 'Mini Project'), ('Main Project', 'Main Project'), ('Live Project', 'Live Project')], default='1', max_length=20),
        ),
    ]
