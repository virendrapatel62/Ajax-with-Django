# Generated by Django 3.1.5 on 2021-03-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_employee_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
