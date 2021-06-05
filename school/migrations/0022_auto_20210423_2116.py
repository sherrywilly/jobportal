# Generated by Django 3.0.5 on 2021-04-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0021_auto_20210418_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='college_aggregate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='college_year_of_passing',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='hsc',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='hsc_aggregate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='hsc_year_of_passing',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='school',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='school_aggregate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='school_year_of_passing',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='education',
            field=models.CharField(choices=[('bca', 'BCA'), ('B-TECH', 'BTECH'), ('MCA', 'MCA'), ('M-TECH', 'M-TECH'), ('EEE', 'EEE'), ('COMPUTER_SCIENCE', 'COMPUTER_SCIENCE'), ('BBA', 'BBA'), ('BCOM', 'B-COM')], max_length=100, null=True),
        ),
    ]
