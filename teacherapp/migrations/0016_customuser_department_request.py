# Generated by Django 5.0.7 on 2024-08-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0015_alter_customuser_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='department_request',
            field=models.BooleanField(default=False),
        ),
    ]
