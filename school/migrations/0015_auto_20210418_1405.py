# Generated by Django 3.0.5 on 2021-04-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_studentextra_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherextra',
            name='joindate',
        ),
        migrations.RemoveField(
            model_name='teacherextra',
            name='salary',
        ),
        migrations.AddField(
            model_name='teacherextra',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]